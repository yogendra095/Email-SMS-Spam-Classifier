import pickle
import numpy as np

with open('Models/vectorizer.pkl','rb') as f:
    tfidf=pickle.load(f)

def vectorize_text(text):
    return tfidf.transform([text]).toarray()