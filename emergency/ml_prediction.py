import joblib
import os
import pandas as pd

MODEL_PATH = os.path.join(os.path.dirname(__file__),'risk_model.pkl')

model = joblib.load(MODEL_PATH)

def predict_risk(
    oxygen_level,
    heart_rate,
    temperature,
    systolic_bp,
    diastolic_bp,
    emergency_type
):
    data = pd.DataFrame([
        {
            'oxygen_level':oxygen_level,
            'heart_rate':heart_rate,
            'temperature':temperature,
            'systolic_bp':systolic_bp,
            'diastolic_bp':diastolic_bp,
            'emergency_type':emergency_type
        }
    ])

    prediction = model.predict(data)[0]
    probabilities = model.predict_proba(data)[0]
    probability = max(probabilities)
    return prediction, probability