import logging
import customtkinter as tk

def log_to_file(service_type, message):
    """
    Log error message to a file
    :param service_type:
    :param message:
    :return:
    """
    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s - %(message)s',
                        filename="InstallationTool.log", encoding='utf-8',
                        level=logging.ERROR)
    logger.error(message)

    match service_type:
        case "http_request_&_install_executable":
            create_error_window("Enable to download or install file(s)")
        case "main":
            create_error_window("Critical error")
        case "create_error_window":
            create_error_window("Critical error")
        case "create_company_logo":
            create_error_window("Enable to display logo")
        case "edit_textbox_finishing":
            create_error_window("Critical error")
        case "edit_textbox_installing":
            create_error_window("Critical error")
        case "edit_textbox_downloading":
            create_error_window("Critical error")
        case "create_textbox":
            create_error_window("Critical error")
        case "create_validate_button":
            create_error_window("Critical error")
        case "create_checkboxes":
            create_error_window("Critical error")
        case _:
            create_error_window("Critical error")

def create_error_window(error_message):
    """
    Create a window when an error occurs
    :param error_message:
    :return:
    """
    try:
        error_window = tk.CTk()
        error_window.title("Erreur")
        error_window.resizable(False, False)
        error_window.geometry("300x150")
        error_window.configure(fg_color="#ffffff")

        label = tk.CTkLabel(error_window, text=error_message, text_color="red", wraplength=280)
        label.pack(padx=20, pady=30)

        # Optional: bouton pour fermer
        close_btn = tk.CTkButton(error_window, text="Fermer", command=error_window.destroy)
        close_btn.pack(pady=10)

        log_to_file("error_window", error_message)
        error_window.mainloop()  # à utiliser seulement si c’est une fenêtre indépendante
    except Exception as e:
        log_to_file("error_window", e)
        create_error_window(e)