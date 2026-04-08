from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model.joblib")

@app.get("/")
def home():
    return {"message": "AI API running"}

from pydantic import BaseModel
from typing import List

class InputData(BaseModel):
    data: List[float]

@app.post("/predict")
def predict(input: InputData):
    prediction = model.predict([input.data])
    return {"prediction": int(prediction[0])}