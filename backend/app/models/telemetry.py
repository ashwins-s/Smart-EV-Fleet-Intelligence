from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    BigInteger,
    DECIMAL,
    String,
    DateTime,
    ForeignKey,
)

from app.database import Base


class Telemetry(Base):
    __tablename__ = "telemetry_data"

    telemetry_id = Column(
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

    battery_percentage = Column(
        DECIMAL(5, 2),
        nullable=False
    )

    battery_temperature = Column(
        DECIMAL(5, 2),
        nullable=False
    )

    motor_temperature = Column(
        DECIMAL(5, 2),
        nullable=False
    )

    speed = Column(
        DECIMAL(6, 2),
        nullable=False
    )

    latitude = Column(
        DECIMAL(10, 7),
        nullable=False
    )

    longitude = Column(
        DECIMAL(10, 7),
        nullable=False
    )

    charging_status = Column(
        String(20),
        nullable=False
    )

    recorded_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )