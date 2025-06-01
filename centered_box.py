from tkinter import *
import customtkinter as ctk

def create_centered_box(root, bg_color="black", box_bg_color="gray", text_color="white", content_fn=None):
    content = ctk.CTkFrame(root, fg_color=bg_color)

    center_box = Frame(content, background=box_bg_color, padx=20, pady=20)
    center_box.place(relx=0.5, rely=0.5, anchor=CENTER)

    if callable(content_fn):
        content_fn(center_box)  # Like rendering children inside a container
    else:
        ctk.CTkLabel(center_box, text="Content here...", text_color=text_color, fg_color=box_bg_color).pack()

    return content
