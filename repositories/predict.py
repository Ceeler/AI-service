from keras.models import load_model
from PIL import ImageOps, Image
import numpy as np
from .base import BaseRepository
from typing import List
from models.predict import Predict


class PredictRepository(BaseRepository):

    async def predict_digit(self, img: Image, filtered: int = 150 ) -> Predict:
        model = self.model

        img = img.resize((28,28))
        
        img = img.convert('L')
        img = ImageOps.invert(img)
        img = np.array(img)
        img[img <= filtered] = 0

        im = Image.fromarray(img)
        im.save("res.jpeg")

        img = img.reshape(1,28,28,1)

        res = model.predict([img])[0]
        
        predict = Predict(
                digit = np.argmax(res),
                accuracy = max(res),

        )

        return predict
