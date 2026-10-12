from datetime import datetime

from sqlalchemy import (
    Column,
    BigInteger,
    Integer,
    String,
    DateTime,
    ForeignKey,
)

from app.database import Base


class Alert(Base):
    __tablename__ = "alerts"

    alert_id = Column(
        BigInteger,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    vehicle_id = Column(
        Integer,
        ForeignKey("vehicles.vehicle_id"),
        nullable=False
    )

    maintenance_risk = Column(
        String(20),
        nullable=False
    )

    message = Column(
        String(255),
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )