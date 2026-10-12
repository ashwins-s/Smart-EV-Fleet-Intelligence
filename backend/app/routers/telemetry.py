
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.telemetry import Telemetry
from app.models.vehicle import Vehicle
from app.models.alert import Alert
from app.schemas.telemetry import TelemetryCreate, TelemetryResponse

from ai.predict_service import predict_maintenance_risk


router = APIRouter()


# Get telemetry history with AI maintenance-risk predictions
@router.get("/telemetry", response_model=list[TelemetryResponse])
def get_telemetry(db: Session = Depends(get_db)):
    telemetry_records = (
        db.query(Telemetry)
        .order_by(Telemetry.recorded_at.desc())
        .all()
    )

    response = []

    for record in telemetry_records:
        try:
            telemetry_data = TelemetryCreate(
                vehicle_id=record.vehicle_id,
                battery_percentage=float(record.battery_percentage),
                battery_temperature=float(record.battery_temperature),
                motor_temperature=float(record.motor_temperature),
                speed=float(record.speed),
                latitude=float(record.latitude),
                longitude=float(record.longitude),
                charging_status=record.charging_status
            )
        except Exception as error:
            print(
                f"Skipping invalid telemetry record "
                f"{record.telemetry_id}: {error}"
            )
            continue

        maintenance_risk = predict_maintenance_risk(
            telemetry_data.battery_percentage,
            telemetry_data.battery_temperature,
            telemetry_data.motor_temperature,
            telemetry_data.speed,
            telemetry_data.charging_status
        )

        response.append({
            **telemetry_data.model_dump(),
            "telemetry_id": record.telemetry_id,
            "recorded_at": record.recorded_at,
            "maintenance_risk": maintenance_risk
        })

    return response


# Create telemetry, predict risk, and avoid duplicate HIGH alerts
@router.post("/telemetry", response_model=TelemetryResponse)
def create_telemetry(
    telemetry: TelemetryCreate,
    db: Session = Depends(get_db)
):
    # Check that the vehicle exists
    vehicle = (
        db.query(Vehicle)
        .filter(Vehicle.vehicle_id == telemetry.vehicle_id)
        .first()
    )

    if vehicle is None:
        raise HTTPException(
            status_code=404,
            detail=f"Vehicle with ID {telemetry.vehicle_id} not found"
        )

    # Predict maintenance risk
    maintenance_risk = predict_maintenance_risk(
        telemetry.battery_percentage,
        telemetry.battery_temperature,
        telemetry.motor_temperature,
        telemetry.speed,
        telemetry.charging_status
    )

    # Save telemetry
    new_data = Telemetry(**telemetry.model_dump())

    try:
        db.add(new_data)
        db.commit()
        db.refresh(new_data)

        # Create a HIGH-risk alert only if none exists for this vehicle
        if maintenance_risk == "HIGH":
            existing_alert = (
                db.query(Alert)
                .filter(
                    Alert.vehicle_id == telemetry.vehicle_id,
                    Alert.maintenance_risk == "HIGH"
                )
                .first()
            )

            if existing_alert is None:
                new_alert = Alert(
                    vehicle_id=telemetry.vehicle_id,
                    maintenance_risk="HIGH",
                    message=(
                        "High maintenance risk detected for vehicle."
                    )
                )

                db.add(new_alert)
                db.commit()

                print("HIGH maintenance alert created.")
            else:
                print(
                    "HIGH maintenance alert already exists. "
                    "Duplicate alert skipped."
                )

    except Exception:
        db.rollback()
        raise

    print("AI Maintenance Risk:", maintenance_risk)

    return {
        **telemetry.model_dump(),
        "telemetry_id": new_data.telemetry_id,
        "recorded_at": new_data.recorded_at,
        "maintenance_risk": maintenance_risk
    }
