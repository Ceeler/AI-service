from keras.models import load_model

class BaseRepository:
    model = load_model('dmnist.h5')
    # def __init__(self):
        