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
