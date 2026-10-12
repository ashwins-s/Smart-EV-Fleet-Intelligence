import pandas as pd
import joblib


# Load trained model
model = joblib.load("ai/maintenance_model.pkl")


def predict_maintenance_risk(
    battery_percentage,
    battery_temperature,
    motor_temperature,
    speed,
    charging_status
):
    # Create input data
    data = pd.DataFrame([
        {
            "battery_percentage": battery_percentage,
            "battery_temperature": battery_temperature,
            "motor_temperature": motor_temperature,
            "speed": speed,
            "charging_status": charging_status
        }
    ])

    # Convert charging status to numeric columns
    data = pd.get_dummies(
        data,
        columns=["charging_status"],
        dtype=int
    )

    # Match the exact columns used during training
    required_columns = [
        "battery_percentage",
        "battery_temperature",
        "motor_temperature",
        "speed",
        "charging_status_Charging",
        "charging_status_Not Charging"
    ]

    data = data.reindex(
        columns=required_columns,
        fill_value=0
    )

    # Make prediction
    prediction = model.predict(data)

    return prediction[0]