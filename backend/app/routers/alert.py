
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.alert import Alert

router = APIRouter()


@router.get("/alerts")
def get_alerts(db: Session = Depends(get_db)):
    alerts = (
        db.query(Alert)
        .order_by(Alert.created_at.desc())
        .all()
    )

    return [
        {
            "alert_id": alert.alert_id,
            "vehicle_id": alert.vehicle_id,
            "maintenance_risk": alert.maintenance_risk,
            "message": alert.message,
            "created_at": alert.created_at
        }
        for alert in alerts
    ]
