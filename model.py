import numpy as np
from sklearn.linear_model import LinearRegression

def train_model():
    hours = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)
    marks = np.array([20,35,45,55,65,75,85,90,95,98])
    model = LinearRegression()
    model.fit(hours, marks)
    return model

def predict_marks(hours):
    model = train_model()
    result = model.predict([[hours]])
    return round(result[0], 2)
