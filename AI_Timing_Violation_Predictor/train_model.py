import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from utils.data_generator import generate_smarter_dataset
import os

if not os.path.exists("data/smarter_timing_dataset.csv"):
    os.makedirs("data", exist_ok=True)
    generate_smarter_dataset()

df = pd.read_csv("data/smarter_timing_dataset.csv")
features = df[["Number_of_Gates", "Maximum_Path_Delay", "Slack", "Operating_Frequency", "Fanout"]]
labels = df["Timing_Violation"]

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print(f"✅ Model trained with accuracy: {accuracy * 100:.2f}%")

os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/trained_model.pkl")
print("✅ Model saved at models/trained_model.pkl")
