from fastapi import FastAPI, HTTPException  
from pydantic import BaseModel  
from pathlib import Path
import pickle
import tensorflow as tf  
from tensorflow.keras.models import load_model  
from tensorflow.keras.preprocessing.sequence import pad_sequences  # type: ignore
import uvicorn 

app = FastAPI(title="Sentiment Analyzer API")

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model.h5"
TOKENIZER_PATH = BASE_DIR / "tokenizer.pkl"

class PatchedEmbedding(tf.keras.layers.Embedding):
    def __init__(self, *args, quantization_config=None, **kwargs):
        super().__init__(*args, **kwargs)

if not MODEL_PATH.exists() or not TOKENIZER_PATH.exists():
    raise FileNotFoundError("Missing model.h5 or tokenizer.pkl in the directory.")

# Load model & tokenizer
model = load_model(
    MODEL_PATH,
    compile=False,
    custom_objects={"Embedding": PatchedEmbedding},
)

with open(TOKENIZER_PATH, "rb") as file:
    tokenizer = pickle.load(file)

maxlen = 200

class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    sentiment: str
    score: float

@app.post("/predict", response_model=SentimentResponse)
async def predict(request: SentimentRequest):
    text = request.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Text is required.")

    seq = tokenizer.texts_to_sequences([text])
    pad = pad_sequences(seq, maxlen=maxlen)

    prediction = model.predict(pad, verbose=0)[0][0]
    sentiment = "Positive" if prediction > 0.5 else "Negative"

    return SentimentResponse(sentiment=sentiment, score=float(prediction))

if __name__ == "__main__":
    uvicorn.run("backend:app", host="0.0.0.0", port=8000, reload=True)
