import joblib

def predict(data):
    cls=joblib.load('dc_model')

    return cls.predict(data)

