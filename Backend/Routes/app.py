from fastapi import FastAPI
from .cors import add_cors
from schemas.validation import Input
from Models.prediction import predict
from fastapi.responses import JSONResponse
app=FastAPI()

add_cors(app)

@app.get("/")
def about():
    return {"About":"This is an API for the prediciton of mail or sms as spam or not spam"}


@app.get("/health")
def health():
    return {'Status':"OK"}

@app.post("/predict")
def check(user_input:Input):
    messages=user_input.message
    try:
       output= predict(messages)
       return JSONResponse(status_code=200,content=output)

    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))