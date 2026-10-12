import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# ==========================================
# 1. Load Training Dataset
# ==========================================

df = pd.read_csv("ai/training_data.csv")

print("Dataset loaded successfully!")
print("Total records:", len(df))


# ==========================================
# 2. Check Dataset
# ==========================================

print("\nFirst 5 records:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())


# ==========================================
# 3. Separate Features and Target
# ==========================================

X = df[
    [
        "battery_percentage",
        "battery_temperature",
        "motor_temperature",
        "speed",
        "charging_status"
    ]
]

y = df["maintenance_risk"]


# ==========================================
# 4. Convert Charging Status to Numbers
# ==========================================

X = pd.get_dummies(
    X,
    columns=["charging_status"],
    dtype=int
)

print("\nFeatures after preprocessing:")
print(X.head())

print("\nFeature columns:")
print(X.columns.tolist())

print("\nTarget values:")
print(y.head())


# ==========================================
# 5. Split Dataset
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nData split completed!")
print("Training records:", len(X_train))
print("Testing records:", len(X_test))


# ==========================================
# 6. Create Random Forest Model
# ==========================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# ==========================================
# 7. Train Model
# ==========================================

model.fit(X_train, y_train)

print("\nRandom Forest model trained successfully!")


# ==========================================
# 8. Save Trained Model
# ==========================================

joblib.dump(model, "ai/maintenance_model.pkl")

print("\nModel saved successfully!")
print("Saved file: ai/maintenance_model.pkl")


# ==========================================
# 9. Make Predictions
# ==========================================

y_pred = model.predict(X_test)


# ==========================================
# 10. Calculate Accuracy
# ==========================================

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:")
print(f"{accuracy * 100:.2f}%")


# ==========================================
# 11. Classification Report
# ==========================================

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# ==========================================
# 12. Confusion Matrix
# ==========================================

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


print("\nModel training and evaluation completed successfully!")