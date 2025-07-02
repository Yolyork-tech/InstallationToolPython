import subprocess
import os

from Services.gui_utils import edit_textbox_installing, create_error_window


def install_executable(app_name, app_data, textbox):
    """
    Installe un exécutable (.exe ou .msi) en mode silencieux.

    :param app_name: Nom du logiciel à installer
    :param app_data: Data contenu dans software.json
    :param textbox: Texte du installer
    :return: Code de retour du processus (0 = succès)
    """
    try:
        filetype = app_data['InstallationType']
        silent_args = app_data['Arg']
        temp_dir = os.environ["TEMP"]
        filepath = os.path.join(temp_dir, "utils", app_data['RegistrationName'])

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

        edit_textbox_installing(textbox, app_name)
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
    except Exception as e:
        create_error_window(e)
        return -1