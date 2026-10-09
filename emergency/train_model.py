import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CSV_PATH = os.path.join(BASE_DIR,'ml_data','emergency_data.csv')
MODEL_PATH = os.path.join(BASE_DIR,'risk_model.pkl')

#load dataset
data = pd.read_csv(CSV_PATH)

features =[
    'oxygen_level',
    'heart_rate',
    'temperature',
    'systolic_bp',
    'diastolic_bp',
    'emergency_type'
]

x = data[features]
y = data['risk_level']

#categorical column
categorical_features = [
    'emergency_type'
]

numeric_features = [
    'oxygen_level',
    'heart_rate',
    'temperature',
    'systolic_bp',
    'diastolic_bp'
]

preprocessor = ColumnTransformer(
    transformers=[
        (
            'category',
            OneHotEncoder(handle_unknown='ignore'),
            categorical_features
        )
    ],
    remainder='passthrough'
)

model = RandomForestClassifier(n_estimators=200,random_state=42,class_weight='balanced')

Pipeline = Pipeline(steps=[('preprocessor',preprocessor),('model',model)])

X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42,stratify=y)
#train
Pipeline.fit(X_train,y_train)
#accuracy
predictions = Pipeline.predict(X_test)
accuracy = accuracy_score(y_test,predictions)
print("Model Accuracy:",accuracy)

#save model
joblib.dump(Pipeline,MODEL_PATH)
print(MODEL_PATH)

