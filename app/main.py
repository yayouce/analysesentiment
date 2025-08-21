from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import re
import nltk
from nltk.corpus import stopwords
from .config import settings
import os
import pandas as pd


nltk.download('stopwords', quiet=True)
stop_words = set(stopwords.words('english'))

app = FastAPI(title=settings.APP_TITLE, description=settings.APP_DESCRIPTION)

class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    sentiment: str
    sentiment_score: float

class Review(BaseModel):
    cleaned_text: str
    sentiment_label: int

try:
    if settings.MODEL_PATH is None or settings.VECTORIZER_PATH is None:
        raise FileNotFoundError()
    model = joblib.load(settings.MODEL_PATH)
    vectorizer = joblib.load(settings.VECTORIZER_PATH)
except FileNotFoundError:
    model = None
    vectorizer = None
    print("ATTENTION: Modèle ou vectorizer non trouvé. L'endpoint /predict ne fonctionnera pas.")


reviews_df = pd.read_parquet(settings.PROCESSED_DATA_PATH)

def traitement_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return ' '.join([word for word in text.split() if word not in stop_words])


@app.get('/')
def read_root():
    return {"status": "API en ligne", "message": "Bienvenue sur l'API d'analyse de sentiments."}




@app.get("/allavis", response_model=List[Review])
def get_avis(skip: int = 0, limit: int = 10):
    """
    Récupère une liste paginée des avis nettoyés depuis la base de données.
    - **limit**: Nombre maximum d'enregistrements à retourner.
    """
    if reviews_df is None:
        raise HTTPException(
            status_code=503, 
            detail="Les données des avis ne sont pas disponibles."
        )
    paginated_df = reviews_df.iloc[skip : skip + limit]
    return paginated_df.to_dict(orient="records")




@app.post('/predict',response_model=SentimentResponse)
def prediction_sentiment(request:SentimentRequest):
    if model is None or vectorizer is None:
        raise HTTPException(
            status_code=503,
            detail="Modèle non disponible. Veuillez entraîner le modèle avant d'utiliser cette API"
        )
    cleaned_text = traitement_text(request.text)
    vectorized_text = vectorizer.transform([cleaned_text])
    print(vectorized_text)
    prediction = model.predict(vectorized_text)[0]
    probabilite =model.predict_proba(vectorized_text[0]).max()
    sentiment = "Positif" if prediction == 1 else "Négatif"
    return SentimentResponse(sentiment=sentiment,sentiment_score=round(float(probabilite),4))




