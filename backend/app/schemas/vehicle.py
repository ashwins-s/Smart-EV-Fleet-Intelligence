from pydantic import BaseModel
from datetime import date


class VehicleResponse(BaseModel):
    vehicle_id: int
    vehicle_number: str
    model: str
    manufacturer: str
    battery_capacity: float
    purchase_date: date | None = None
    status: str
    driver_id: int | None = None

    class Config:
        from_attributes = True


class VehicleCreate(BaseModel):
    vehicle_number: str
    model: str
    manufacturer: str
    battery_capacity: float
    purchase_date: date | None = None
    status: str
    driver_id: int | None = None