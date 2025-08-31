import joblib
import numpy as np
import os

# Load model and columns
model_path = os.path.join(os.path.dirname(__file__), "carbon_model.pkl")
columns_path = os.path.join(os.path.dirname(__file__), "model_columns.pkl")

model = joblib.load(model_path)
model_columns = joblib.load(columns_path)

def predict_footprint(user_input: dict):
    input_vector = np.zeros(len(model_columns))

    for feature, value in user_input.items():
        if feature in model_columns:
            index = model_columns.index(feature)
            input_vector[index] = value

    return model.predict([input_vector])[0]
