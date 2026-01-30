import numpy as np
import pandas as pd
from .vectorizer import vectorize_text
import pickle

with open('Models/model.pkl','rb') as f:
    model=pickle.load(f)

def predict(msg:str):
    X=vectorize_text(msg)
    prediction=model.predict(X)
    if prediction==1:
        return {"prediction":"Spam"}
    else:
        return {"prediction":"Not Spam"}