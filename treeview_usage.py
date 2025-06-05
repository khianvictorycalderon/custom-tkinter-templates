import customtkinter as ctk
from tkinter import *
from treeview import create_treeview

app = ctk.CTk()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height}+0+0")
app.state("zoomed")

# Sample column and data
sample_columns = ["Name", "Age", "Gender", "Address"]
sample_data = [
    ["Alice", 17, "Female", "Brook Street"],
    ["John", 22, "Male", "Maple Avenue"],
    ["Sophia", 19, "Female", "Elm Street"],
    ["Liam", 25, "Male", "Oak Drive"],
    ["Emma", 21, "Female", "Pine Road"],
    ["Noah", 18, "Male", "Cedar Lane"],
    ["Olivia", 20, "Female", "Main Street"],
    ["James", 23, "Male", "Park Avenue"],
    ["Isabella", 24, "Female", "Sunset Boulevard"],
    ["Lucas", 26, "Male", "Highland Road"],
    ["Mia", 22, "Female", "Riverside Drive"],
    ["Benjamin", 19, "Male", "Lakeview Street"],
    ["Amelia", 18, "Female", "Hilltop Road"],
    ["Elijah", 21, "Male", "Birch Avenue"],
    ["Charlotte", 23, "Female", "Forest Street"],
    ["Logan", 20, "Male", "Chestnut Drive"],
    ["Ava", 25, "Female", "Valley Road"],
    ["Ethan", 24, "Male", "Hawthorn Street"],
    ["Harper", 22, "Female", "Willow Way"],
    ["Daniel", 26, "Male", "Magnolia Lane"]
]

create_treeview(app, columns=sample_columns, data=sample_data).pack(fill = BOTH)

app.mainloop()
