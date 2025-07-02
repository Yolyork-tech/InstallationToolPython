import subprocess
import os


def install_executable(filepath, filetype, silent_args=None):
    """
    Installe un exécutable (.exe ou .msi) en mode silencieux.

    :param filepath: Chemin complet du fichier exécutable
    :param silent_args: Liste d'arguments pour installation silencieuse (ex: ["/S"] ou ["/quiet"])
    :return: Code de retour du processus (0 = succès)
    """
    if not os.path.exists(filepath):
        print(f"Fichier non trouvé : {filepath}")
        return -1

    if not silent_args:
        # Choix par défaut selon l'extension
        if filepath.endswith(".exe"):
            silent_args = ["/S"]  # très courant
        elif filepath.endswith(".msi"):
            silent_args = ["/quiet", "/norestart"]
        else:
            print("Extension de fichier non prise en charge.")
            return -1

    try:
        print(f"▶Lancement de l'installation de {os.path.basename(filepath)}...")
        if filetype == "Msiexec":
            result = subprocess.run(["msiexec", "/i", filepath] + silent_args.split(), check=True)
        elif filetype.lower() == "exe":
            result = subprocess.run([filepath] + silent_args.split(), check=True)
        else:
            print("Type d'installation non supporté.")
            return -1

        print(f"Installation terminée (code {result.returncode})")
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation : {e}")
        return e.returncode
