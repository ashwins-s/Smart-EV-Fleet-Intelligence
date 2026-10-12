import pandas as pd
import joblib


# ==========================================
# 1. Load Trained Model
# ==========================================

model = joblib.load("ai/maintenance_model.pkl")

print("Trained model loaded successfully!")


# ==========================================
# 2. New EV Telemetry Data
# ==========================================

new_data = pd.DataFrame([
    {
        "battery_percentage": 25,
        "battery_temperature": 42,
        "motor_temperature": 72,
        "speed": 55,
        "charging_status": "Not Charging"
    }
])


# ==========================================
# 3. Preprocess New Data
# ==========================================

new_data = pd.get_dummies(
    new_data,
    columns=["charging_status"],
    dtype=int
)


# Make sure the columns match the training data
required_columns = [
    "battery_percentage",
    "battery_temperature",
    "motor_temperature",
    "speed",
    "charging_status_Charging",
    "charging_status_Not Charging"
]

new_data = new_data.reindex(
    columns=required_columns,
    fill_value=0
)


# ==========================================
# 4. Predict Maintenance Risk
# ==========================================

prediction = model.predict(new_data)


# ==========================================
# 5. Display Result
# ==========================================

print("\nNew EV Telemetry:")
print(new_data)

print("\nPredicted Maintenance Risk:")
print(prediction[0])