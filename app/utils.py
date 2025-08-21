import os
import glob


# Fonction pour trouver le fichier le plus récent dans un dossier
def find_latest_file(directory, pattern):
    try:
        files = glob.glob(os.path.join(directory, pattern))
        if not files:
            return None
        return max(files, key=os.path.getctime)
    except Exception:
        return None
    


