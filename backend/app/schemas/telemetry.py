
from datetime import datetime
from pydantic import BaseModel, Field


class TelemetryCreate(BaseModel):
    vehicle_id: int = Field(gt=0)

    battery_percentage: float = Field(ge=0, le=100)
    battery_temperature: float = Field(ge=-50, le=150)
    motor_temperature: float = Field(ge=-50, le=250)
    speed: float = Field(ge=0, le=300)

    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)

    charging_status: str = Field(
        min_length=1,
        max_length=20
    )


class TelemetryResponse(TelemetryCreate):
    telemetry_id: int
    recorded_at: datetime
    maintenance_risk: str

    class Config:
        from_attributes = True

