import customtkinter as tk
import os

from Services.CustomHttpsRequest import http_request
from Services.readJson import read_json
from Services.gui_utils import create_checkboxes, create_validate_button
from Services.AppInstallationService import install_executable

def main():
    #Main window
    root = tk.CTk()
    root.title("Applications")
    root.resizable(False, False)
    root.geometry("500x500")
    root.configure(background="#ffffff")

    #Create checkbox
    software_json = read_json("Json_files/software.json")
    app_vars = {}
    for app_name in software_json:
        app_vars[app_name] = tk.BooleanVar()
    frame = tk.CTkFrame(root, fg_color="#ffffff", border_color="#ffffff")
    frame.pack(padx=10, pady=10)
    create_checkboxes(frame, app_vars)

    def on_validate():
        selected = [name for name, var in app_vars.items() if var.get()]

        if not selected:
            print("Aucune application sélectionnée.")
            return

        for app_name in selected:
            if app_name in software_json:
                app_data = software_json[app_name]
                http_request(app_data['RegistrationName'], app_data['Url'])
                temp_dir = os.environ["TEMP"]
                filepath = os.path.join(temp_dir, "utils", app_data['RegistrationName'])
                install_executable(filepath, app_data['InstallationType'] , app_data['Arg'])
            else:
                print(f"{app_name} n'existe pas dans le JSON.")

    create_validate_button(root, on_validate)

    root.mainloop()

if __name__ == "__main__":
    main()
