from tkinter import *
from PIL import Image
import customtkinter as tk
import os
import sys
from Services.CustomLogger import log_to_file

#White background
bg_color_white = "#ffffff"


def create_checkboxes(frame, app_vars):
    """
    Create checkboxes for app installation
    :param frame:
    :param app_vars:
    :return:
    """
    try:
        # Canvas pour scroller
        canvas = tk.CTkCanvas(frame, width=450, height=200)
        canvas.configure(highlightcolor="black", highlightthickness=1, bg=bg_color_white)
        scrollbar = tk.CTkScrollbar(frame, command=canvas.yview)
        scrollbar.configure(bg_color=bg_color_white)
        scroll_frame = tk.CTkFrame(canvas, fg_color=bg_color_white, border_color=bg_color_white)

        scroll_frame.bind(
            "<Configure>",
            lambda a: canvas.configure(
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
    except Exception as e:
        log_to_file("create_checkboxes", e)

def create_validate_button(root, on_validate):
    """
    Create validate button for app installation
    :param root:
    :param on_validate:
    :return:
    """
    try:
        btn = tk.CTkButton(root, text="Validate", command=on_validate)
        btn.pack(pady=10)
    except Exception as e:
        log_to_file("create_validate_button", e)

# Create Textbox
def create_textbox(root):
    """
    Create textbox for display downloading/installing state
    :param root:
    :return:
    """
    try:
        textbox = tk.CTkTextbox(root, width=300, height=20)
        textbox.pack(padx=1, pady=1)
        textbox.insert(tk.END, text='Cochez les cases pour installer les logiciels')
        textbox.configure(state=tk.DISABLED)
        return textbox
    except Exception as e:
        log_to_file("create_textbox", e)
        return -1

def edit_textbox_downloading(textbox):
    """
    Edit textbox downloading state
    :param textbox:
    :return:
    """
    try:
        textbox.configure(state=tk.NORMAL)
        textbox.delete(1.0, tk.END)
        textbox.insert(tk.END, "Téléchargement de(s) logiciel(s)")
        textbox.configure(state=tk.DISABLED)
    except Exception as e:
        log_to_file("edit_textbox_downloading", e)

def edit_textbox_installing(textbox, app_name):
    """
    Edit textbox installing state
    :param textbox:
    :param app_name:
    :return:
    """
    try:
        textbox.configure(state=tk.NORMAL)
        textbox.delete(1.0, tk.END)
        textbox.insert(tk.END, "Installation de " + app_name)
        textbox.configure(state=tk.DISABLED)
    except Exception as e:
        log_to_file("edit_textbox_installing", e)

def edit_textbox_finishing(textbox):
    """
    Edit textbox finishing state
    :param textbox:
    :return:
    """
    try:
        textbox.configure(state=tk.NORMAL)
        textbox.delete(1.0, tk.END)
        textbox.insert(tk.END, "Installation terminée")
        textbox.configure(state=tk.DISABLED)
    except Exception as e:
        log_to_file("edit_textbox_finishing", e)

def create_company_logo(gui_ref):
    """
    Create company logo
    :param gui_ref:
    :return:
    """
    try:
        company_logo = tk.CTkImage(light_image=Image.open(resource_path("company_logo.png")),
                    dark_image=Image.open(resource_path("company_logo.png")),
                    size=(100, 54))
        img_label = tk.CTkLabel(gui_ref, text="", image=company_logo)
        img_label.pack(padx=10, pady=10)
    except Exception as e:
        log_to_file("create_company_logo", e)

def resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and for PyInstaller.
    :param relative_path:
    :return:
    """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)