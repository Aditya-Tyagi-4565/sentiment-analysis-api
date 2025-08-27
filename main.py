from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = FastAPI(title="Sentiment Analysis API", description="An API to predict sentiment of customer reviews.")

with open('artifacts/tokenizer.pkl','rb') as f:
    tokenizer = pickle.load(f)

model = load_model('artifacts/sentiment_model.h5')
MAX_LEN = 150

class ReviewRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Sentiment Analysis API!"}

@app.post("/predict")
def predict_sentiment(request: ReviewRequest):
    text = request.text
    seq = tokenizer.texts_to_sequences([text])
    padded_seq = pad_sequences(seq, maxlen=MAX_LEN,padding='post',truncating='post')
    prediction_proba = model.predict(padded_seq)[0][0]

    sentiment = "Positive" if prediction_proba > 0.5 else "Negative"

    return {
        "text": text,
        "sentiment": sentiment,
        "probability": float(prediction_proba)
    }
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)