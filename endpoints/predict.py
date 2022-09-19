from typing import List
from fastapi import APIRouter, File, UploadFile, Depends
from repositories.predict import PredictRepository
from .depends import get_predict_repository
from io import BytesIO
from PIL import Image
from models.predict import Predict

router = APIRouter()

@router.post("/", response_model=Predict)
async def predict(
    filtered: int = 150,
    file: UploadFile = File(),
    predicts: PredictRepository =  Depends(get_predict_repository)):

    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    img = await read_imagefile(await file.read())
    return await predicts.predict_digit(img, filtered)

async def read_imagefile(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image
