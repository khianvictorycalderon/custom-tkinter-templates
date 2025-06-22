import customtkinter as ctk
from tkinter import *
from ctk_temp_flex_text import create_flex_text

app = ctk.CTk()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height}+0+0")
app.state("zoomed")

data = {
    "logo": ["BreadCo.png", "FreshLoaf.png"],
    "contacts": [
        ["orders@breadco.com", "billing@breadco.com"],
        ["support@breadco.com", "careers@breadco.com"]
    ],
    "address": [
        ["123 Baker Street", "Suite B"],
        ["Crustville, Doughland", "+1 (555) 987-6543"]
    ],
    "legal": [
        "BreadCo Artisan Bakery Ltd.", "Terms and Conditions · Privacy Policy"
    ],
    "legal2": [
        "BreadCo Artisan Bakery Ltd.", "Terms and Conditions · Privacy Policy"
    ],
    "Clickable Link": [
        "https://google.com/", "https://youtube.com/"
    ]
}

create_flex_text(app, data).pack(fill = BOTH)

app.mainloop()