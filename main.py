import tkinter as tk
from Services.readJson import read_json
from Services.gui_utils import create_checkboxes, create_validate_button

def display_selection(app_vars):
    for app_name, var in app_vars.items():
        if var.get() == 1:
            print(f"{app_name} selected")

def main():
    data = read_json("Json_files/software.json")

    root = tk.Tk()
    root.geometry("500x500")
    root.resizable(False, False)
    root.title("Application Selection")

    app_vars = {app_name: tk.IntVar() for app_name in data.keys()}

    create_checkboxes(root, app_vars)
    create_validate_button(root, lambda: display_selection(app_vars))

    root.mainloop()

if __name__ == "__main__":
    main()
