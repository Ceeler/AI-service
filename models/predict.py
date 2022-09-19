from pydantic import BaseModel
from PIL import Image

class Predict(BaseModel):
    digit: float
    accuracy: float