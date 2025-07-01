import tkinter as tk

def create_checkboxes(root, app_vars):
    for app_name, var in app_vars.items():
        cb = tk.Checkbutton(root, text=app_name, variable=var)
        cb.pack(anchor="w")

def create_validate_button(root, on_validate):
    btn = tk.Button(root, text="Validate", command=on_validate)
    btn.pack(pady=10)
