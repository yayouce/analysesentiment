Un projet complet de Machine Learning démontrant le cycle de vie de bout en bout : de l'analyse exploratoire et l'entraînement d'un modèle sur le dataset Yelp à son déploiement en production via une **API RESTful performante, documentée et conteneurisée**.

Ce projet simule un cas d'usage à forte valeur ajoutée pour toute plateforme d'e-commerce ou e-agence. En analysant automatiquement des milliers d'avis clients, de commentaires sur les réseaux sociaux ou de retours produits, cette API permet de transformer le feedback textuel non structuré en indicateurs de performance exploitables. Elle offre la capacité de :

- **Détection précoce des risques de résiliation** en identifiant les clients exprimant une insatisfaction, même faible
- **Prioriser les actions du service client en identifiant instantanément les clients les plus mécontents**.
- **Détecter en temps réel les problèmes sur un produit ou un service** (bugs, défauts de livraison, etc.).
- **Mesurer l'impact d'une campagne marketing** en suivant l'évolution du sentiment général.
- Analyser la concurrence en appliquant le même modèle à leurs avis publics.
Il met en évidence mes compétences en Data Science, Machine Learning Engineering et MLOps pour construire des solutions qui répondent directement aux enjeux de la satisfaction client et de l'e-réputation.

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
