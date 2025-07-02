import requests as http
import os

def http_request(app_name, url):
    temp_dir = os.environ["TEMP"]  # Récupère le vrai chemin temporaire
    save_path = os.path.join(temp_dir, "utils", app_name)
    try:
        response = http.get(url, stream=True)
        print(f"Statut HTTP : {response.status_code}")
        with open(save_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
    except http.RequestException as e:
        print(f"Erreur de requête : {e}")
