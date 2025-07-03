import threading

from Services.CustomHttpsRequest import http_request
from Services.readJson import read_json
from Services.gui_utils import *

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
    textbox = create_textbox(root)

    #Create company logo
    create_company_logo(root)

    def install_app(name, app_data):
        from Services.AppInstallationService import install_executable
        return install_executable(name, app_data, textbox)

    # THREAD WORKER PRINCIPAL
    def download_and_install_worker(selected):
        try:
            download_threads = []

            for name in selected:
                if name in software_json:
                    app_data = software_json[name]
                    t = threading.Thread(target=http_request, args=(name, app_data))
                    t.start()
                    download_threads.append((t, name, app_data))

            #Attendre tous les téléchargements (dans ce thread, pas l'UI)
            edit_textbox_downloading(textbox)
            for t, _, _ in download_threads:
                t.join()

            # Installer les apps une par une
            for _, name, app_data in download_threads:
                result_install = install_app(name, app_data)
                if result_install >= 0:
                    edit_textbox_finishing(textbox)
        except Exception as e:
            log_to_file("http_request_&_install_executable", e)

    def on_validate():
        selected = [name for name, var in app_vars.items() if var.get()]
        if not selected:
            return

        # Lancer toute la logique dans un thread de fond
        threading.Thread(target=download_and_install_worker, args=(selected,), daemon=True).start()

    create_validate_button(root, on_validate)
    root.mainloop()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log_to_file("main", e)