import customtkinter as ctk
from tkinter import Tk, messagebox
from entry_dropdown_multiple_buttons import create_entry_dropdown_multiple_buttons  # adjust if the function is in same file

app = ctk.CTk()
app.geometry("600x400")
app.title("Multi-Button Form Example")

variables = {}

def add_action():
    values = {k: v.get() for k, v in variables.items()}
    print("Add clicked:", values)
    messagebox.showinfo("Add", f"Added:\n{values}")

def edit_action():
    values = {k: v.get() for k, v in variables.items()}
    print("Edit clicked:", values)
    messagebox.showinfo("Edit", f"Edited:\n{values}")

def remove_action():
    values = {k: v.get() for k, v in variables.items()}
    print("Remove clicked:", values)
    messagebox.showinfo("Remove", f"Removed:\n{values}")

data = {
    "Name": "text_only",
    "Email": "email",
    "Age": "number_positive",
    "Gender": ["Male", "Female", "Other"]
}

buttons = {
    "Add": add_action,
    "Edit": edit_action,
    "Remove": remove_action
}

form = create_entry_dropdown_multiple_buttons(
    root=app,
    data=data,
    col_per_rows=2,
    variable=variables,
    buttons=buttons,
    label_color="white",
    input_bg_color="#f0f0f0",
    input_text_color="black"
)

form.pack(padx=20, pady=20, fill="both", expand=True)
app.mainloop()