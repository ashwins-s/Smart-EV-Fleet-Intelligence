from fastapi import FastAPI
from sqlalchemy import text

from app.database import engine
from app.routers import vehicle
from app.routers import telemetry
from app.routers import alert


app = FastAPI(
    title="Smart EV Fleet Intelligence API",
    description="Backend API for EV Fleet Monitoring and Predictive Maintenance",
    version="1.0.0"
)


app.include_router(vehicle.router)
app.include_router(telemetry.router)
app.include_router(alert.router)


@app.get("/")
def home():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "success",
            "message": "Connected to MySQL successfully!"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }