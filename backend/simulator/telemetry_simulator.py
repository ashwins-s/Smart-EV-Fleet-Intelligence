import requests
import random
import time

API_URL = "http://127.0.0.1:8000/telemetry"

battery = 100.0

while True:

    battery = max(10, battery - random.uniform(0.2, 1.0))

    data = {
        "vehicle_id": 1,
        "battery_percentage": round(battery, 2),
        "battery_temperature": round(random.uniform(28, 45), 2),
        "motor_temperature": round(random.uniform(35, 80), 2),
        "speed": round(random.uniform(0, 100), 2),
        "latitude": round(11.0168 + random.uniform(-0.01, 0.01), 7),
        "longitude": round(76.9558 + random.uniform(-0.01, 0.01), 7),
        "charging_status": "Charging" if battery < 20 else "Not Charging"
    }

    try:
        response = requests.post(API_URL, json=data)
        print("Status Code:", response.status_code)
        print("Response:", response.text)
    except Exception as e:
        print("Error:", e)

    time.sleep(10)