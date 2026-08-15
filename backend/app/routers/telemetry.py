from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.telemetry import Telemetry
from app.schemas.telemetry import TelemetryCreate, TelemetryResponse

router = APIRouter()


@router.get("/telemetry", response_model=list[TelemetryResponse])
def get_telemetry(db: Session = Depends(get_db)):
    telemetry = db.query(Telemetry).all()
    return telemetry


@router.post("/telemetry", response_model=TelemetryResponse)
def create_telemetry(
    telemetry: TelemetryCreate,
    db: Session = Depends(get_db)
):
    new_data = Telemetry(**telemetry.dict())

    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return new_data