from fastapi import Depends, HTTPException, status
from repositories.predict import PredictRepository

def get_predict_repository() -> PredictRepository:
    return PredictRepository()
