import customtkinter as tk

bg_color_white = "#ffffff"

def create_checkboxes(frame, app_vars):
    # Canvas pour scroller
    canvas = tk.CTkCanvas(frame, width=450, height=200)
    canvas.configure(highlightcolor="black", highlightthickness=1, bg=bg_color_white)
    scrollbar = tk.CTkScrollbar(frame, command=canvas.yview)
    scrollbar.configure(bg_color=bg_color_white)
    scroll_frame = tk.CTkFrame(canvas, fg_color=bg_color_white, border_color=bg_color_white)

    scroll_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Ajout des checkbuttons
    for app_name, var in app_vars.items():
        cb = tk.CTkCheckBox(scroll_frame, text=app_name, variable=var, bg_color=bg_color_white)
        cb.pack(fill="x", anchor="w", padx=2, pady=5)

    canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)
    scrollbar.pack(side="right", fill="y")

def create_validate_button(root, on_validate):
    btn = tk.CTkButton(root, text="Validate", command=on_validate)
    btn.pack(pady=10)

# Create Textbox
def create_textbox(root):
    textbox = tk.CTkTextbox(root, width=300, height=20)
    textbox.pack(padx=1, pady=1)
    textbox.insert(tk.END, text='Cochez les cases pour installer les logiciels')
    textbox.configure(state=tk.DISABLED)
    return textbox

def edit_textbox_downloading(textbox):
    textbox.configure(state=tk.NORMAL)
    textbox.delete(1.0, tk.END)
    textbox.insert(tk.END, "Téléchargement de(s) logiciel(s)")
    textbox.configure(state=tk.DISABLED)

def edit_textbox_installing(textbox, app_name):
    textbox.configure(state=tk.NORMAL)
    textbox.delete(1.0, tk.END)
    textbox.insert(tk.END, "Installation de " + app_name)
    textbox.configure(state=tk.DISABLED)

def edit_textbox_finishing(textbox):
    textbox.configure(state=tk.NORMAL)
    textbox.delete(1.0, tk.END)
    textbox.insert(tk.END, "Installation terminée")
    textbox.configure(state=tk.DISABLED)

def create_error_window(error_message):
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

    error_window.mainloop()  # à utiliser seulement si c’est une fenêtre indépendante