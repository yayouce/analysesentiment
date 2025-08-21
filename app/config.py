from pydantic_settings import BaseSettings
import os
import glob

from .utils import find_latest_file

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "models")



# Trouver dynamiquement les derniers fichiers de modèle et de vectorizer
latest_model_path = find_latest_file(MODELS_DIR, "sentiment_model_*.joblib")
latest_vectorizer_path = find_latest_file(MODELS_DIR, "tfidf_vectorizer_*.joblib")



class Settings(BaseSettings): 
    APP_TITLE: str = "Analyse de sentiment des users d'une plateforme de mets"
    APP_DESCRIPTION: str = "API pour prédire le sentiment d'un avis Yelp (Positif/Négatif)"
    MODEL_PATH: str = latest_model_path
    VECTORIZER_PATH: str = latest_vectorizer_path
    PROCESSED_DATA_PATH: str = os.path.join(BASE_DIR, "data/processed/data_cleaned01.parquet")

settings = Settings()