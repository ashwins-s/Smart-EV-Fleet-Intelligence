from datetime import datetime
from pydantic import BaseModel


class TelemetryCreate(BaseModel):
    vehicle_id: int
    battery_percentage: float
    battery_temperature: float
    motor_temperature: float
    speed: float
    latitude: float
    longitude: float
    charging_status: str


class TelemetryResponse(TelemetryCreate):
    telemetry_id: int
    recorded_at: datetime

    class Config:
        from_attributes = True