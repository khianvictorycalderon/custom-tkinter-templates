from tkinter import *
import customtkinter as ctk
from editable_list import create_editable_list

app = ctk.CTk()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height}+0+0")
app.state("zoomed")

columns = {
    "Name": "text",
    "Last Name": "text",
    "Address": "text",
    "Age": "number_positive",
    "Weight": "number",
    "Department": ["Department 1", "Department 2"]
}

sample_list = [
    ["John", "Doe", "Street 123", "25", "70", "Department 1"],
    ["Jake", "Zyrus", "Street 456", "30", "80", "Department 2"]
]

def my_save_callback(_):
    print() # New Empty Line
    for row in sample_list:
        print(row)

create_editable_list(app, columns=columns, data_list=sample_list, on_save=my_save_callback).pack(expand=True, fill=BOTH)

app.mainloop()