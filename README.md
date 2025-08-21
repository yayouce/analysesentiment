Un projet complet de Machine Learning démontrant le cycle de vie de bout en bout : de l'analyse exploratoire et l'entraînement d'un modèle sur le dataset Yelp à son déploiement en production via une **API RESTful performante, documentée et conteneurisée**.

Ce projet a été conçu pour simuler un cas d'usage réel d'entreprise : fournir un service de Machine Learning capable de classifier le sentiment d'un texte en temps réel. Il met en évidence les compétences clés en **Data Science**, **Machine Learning Engineering** et **MLOps**.

###  Fonctionnalités Clés

*   **Workflow ML Complet :** Analyse, nettoyage des données, benchmark de modèles (Régression Logistique vs LightGBM) et sauvegarde des artefacts.
*   **API RESTful Performante :** Construite avec **FastAPI** pour des performances élevées et une faible latence.
*   **Documentation Automatique :** Génération interactive de la documentation d'API (Swagger UI & ReDoc) pour une intégration et des tests facilités.
*   **Conteneurisation Complète :** L'application est entièrement conteneurisée avec **Docker** et orchestrée avec **Docker Compose** pour une reproductibilité et un déploiement sans faille.
*   **Exploration des Données via l'API :** Un endpoint `GET /reviews` avec **pagination** pour explorer les données nettoyées qui ont servi à l'entraînement.
*   **Code Propre et Modulaire :** Le code de l'API est structuré avec une séparation claire entre la configuration, la logique métier et les utilitaires.

---


#### Prérequis
*   Git
*   Docker
*   Docker Compose

#### Installation & Lancement

1.  **Clonez le dépôt :**
    ```bash
    git clone https://..... le repos
    naviguez vers le repertoire
    ```

2.  **Téléchargez les données brutes :**
    (Le notebook peut le faire automatiquement, mais l'utilisation du script est recommandée)
    ```bash
    # Assurez-vous d'avoir configuré votre API Kaggle au préalable
    chmod +x download_data.sh
    ./download_data.sh
    ```

3.  **Entraînez le modèle :**
    Exécutez le notebook `notebooks/01_data_exploration_and_model_training.ipynb`. Cela générera les données traitées et les fichiers du modèle (`.joblib`).

4.  **Lancez l'API avec Docker Compose :**
    ```bash
    docker-compose up
    ```
    *(La première construction peut prendre quelques minutes pour télécharger les images et installer les dépendances.)*

5.  **Explorez l'API !**
    *   **Documentation Interactive (Swagger UI) :** [http://localhost:8000/docs](http://localhost:8000/docs)
    *   **Documentation Alternative (ReDoc) :** [http://localhost:8000/redoc](http://localhost:8000/redoc)

---
