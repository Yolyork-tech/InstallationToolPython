import requests
from lxml import html

def find_latest_file_url(base_url, extension):
    try:
        if extension == 'Msiexec':
            extension = '.msi'
        elif extension == 'Exe':
            extension = '.exe'
        response = requests.get(base_url)
        response.raise_for_status()
        tree = html.fromstring(response.content)
        hrefs = tree.xpath('//a/@href')

        # Filtrer les liens "parents" ../
        hrefs = [href for href in hrefs if not href.startswith('..')]

        # Cas 2 : présence de sous-dossiers (liens finissant par /)
        subfolders = [href for href in hrefs if href.endswith('/')]

        if subfolders:
            # On suppose que ce sont des versions, on prend la dernière (tri alphabétique)
            latest_subfolder = sorted(subfolders)[-1]
            version_url = base_url + latest_subfolder
            # Requête dans ce sous-dossier
            response2 = requests.get(version_url)
            response2.raise_for_status()
            tree2 = html.fromstring(response2.content)
            files = tree2.xpath('//a/@href')
            # Chercher fichier correspondant à l’extension
            for f in files:
                if f.endswith(extension):
                    return version_url + f
            raise ValueError(f"Aucun fichier {extension} trouvé dans {version_url}")

        else:
            # Cas 1 : pas de sous-dossiers, chercher directement le fichier
            for href in hrefs:
                if href.endswith(extension):
                    return base_url + href
            raise ValueError(f"Aucun fichier {extension} trouvé dans {base_url}")

    except Exception as e:
        print(f"Erreur lors de la récupération du fichier : {e}")
        return None
