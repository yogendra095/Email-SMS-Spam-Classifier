import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
ps=PorterStemmer()
def transform_text(text:str):
    text=text.lower()
    text=re.findall(r'[a-z0-9]+',text)
    y=[]
    for i in text:
        if i not in stopwords.words('english'):
            y.append(i)
    
    text=y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


# print(transform_text("Did you complete you work?"))