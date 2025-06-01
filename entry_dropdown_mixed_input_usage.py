from tkinter import *
import customtkinter as ctk
from entry_dropdown_mixed_input import create_entry_dropdown

# Size templates
app = ctk.CTk()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height}+0+0")
app.update()
app.state("zoomed")

input_vars = {}
input_fields = {
    "Name": "text_only",
    "Age":  "number",
    "Email": "email",
    "Type": ["Excellent", "Good", "Fair"],
    "Agenda": "text",
    "Blah Blah": "number",
    "SKAFIASKFOSKFOASKOFA": "text",
    "Department": ["Department 1", "Department 2"],
    "Gender": ["Male", "Female"],
    "Password": "password"
}

def print_all_values():
    for key, var in input_vars.items():
        print(f"{key}: {var.get()}")

create_entry_dropdown(
    app, 
    input_fields, 
    col_per_rows=2, 
    input_bg_color="#CBE5F7",
    input_text_color="#151D41",
    variable=input_vars,
    button_label="Print all data",
    on_submit=print_all_values
).pack(fill = BOTH)

app.mainloop()