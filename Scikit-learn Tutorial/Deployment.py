from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from pydantic import Field
import joblib
import numpy as np

app = FastAPI()

# Load the pre-trained model
loaded_pipeline = joblib.load('pipeline.joblib')

@app.get("/")                    
def read_items(): 
   return "Welcome to the CMP-3.5 Model"

# Input Schema
class Flower(BaseModel):
    feats: List[float] = Field(..., example="[1.0, 2.0, 3.0, 4.0]")

# Output Schema
class Prediction(BaseModel):
    pred : str = Field(..., title="Flower Prediction", example="Setosa")


@app.post("/predict_flower", response_model=Prediction)         # POST to /predict_flower
def predict_flower(featuresObj: Flower):
    try:
        # Convert input features to numpy array
        x = np.array(featuresObj.feats)
        x = x[np.newaxis, :]  # Reshape for prediction
        pred = loaded_pipeline.predict(x)
        return {"pred": str(pred[0])}
    except Exception as e:
        return {"error": str(e)}