from tkinter import *
import customtkinter as ctk
from editable_list import create_editable_list, ArrayVar

# Size templates
app = ctk.CTk()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height}+0+0")
app.update()
app.state("zoomed")

sample_list = ArrayVar(value=[
    ["John", "Doe"],
    ["Jake", "Zyrus"],
    ["Paul", "Walker"]
])

def my_save_callback(data):
    for row in data:
        print(row, ",")

create_editable_list(app, data_var=sample_list, column_per_rows=5, on_save=my_save_callback).pack(expand=True, fill=BOTH)

app.mainloop()