import pandas as pd
import random

data = []

for _ in range(2000):

    battery_percentage = round(random.uniform(10, 100), 2)
    battery_temperature = round(random.uniform(28, 50), 2)
    motor_temperature = round(random.uniform(35, 95), 2)
    speed = round(random.uniform(0, 100), 2)

    charging_status = random.choice([
        "Charging",
        "Not Charging"
    ])

    # Prototype maintenance-risk rules
    if (
        battery_temperature >= 46
        or motor_temperature >= 85
        or battery_percentage <= 20
    ):
        maintenance_risk = "HIGH"

    elif (
        battery_temperature >= 40
        or motor_temperature >= 70
        or battery_percentage <= 40
    ):
        maintenance_risk = "MEDIUM"

    else:
        maintenance_risk = "LOW"

    data.append([
        battery_percentage,
        battery_temperature,
        motor_temperature,
        speed,
        charging_status,
        maintenance_risk
    ])


df = pd.DataFrame(data, columns=[
    "battery_percentage",
    "battery_temperature",
    "motor_temperature",
    "speed",
    "charging_status",
    "maintenance_risk"
])

df.to_csv("ai/training_data.csv", index=False)

print("Training dataset created successfully!")
print("Total records:", len(df))
print("\nRisk distribution:")
print(df["maintenance_risk"].value_counts())