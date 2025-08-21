#!/bin/bash
set -e
TARGET_DIR="../data/raw"
echo "Téléchargement du dataset Yelp via l'API Kaggle"

kaggle datasets download -d yelp-dataset/yelp-dataset -p "$TARGET_DIR" --unzip
echo "Téléchargement et décompression terminés"

echo "Nettoyage du fichier .zip..."
rm "$TARGET_DIR/yelp-dataset.zip"

echo "--- Données prêtes dans le dossier $TARGET_DIR ---"
