from sqlalchemy import Column, Integer, String, DECIMAL, Date, ForeignKey
from app.database import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    vehicle_id = Column(Integer, primary_key=True, index=True)

    vehicle_number = Column(String(20), unique=True, nullable=False)

    model = Column(String(100), nullable=False)

    manufacturer = Column(String(100), nullable=False)

    battery_capacity = Column(DECIMAL(5, 2), nullable=False)

    purchase_date = Column(Date)

    status = Column(String(20), nullable=False)

    driver_id = Column(Integer, ForeignKey("drivers.driver_id"))
    