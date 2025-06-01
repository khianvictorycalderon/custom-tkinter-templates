from tkinter import *
import customtkinter as ctk

# Size templates
app = ctk.CTk()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height}+0+0")
app.update()
app.state("zoomed")
app.title("Set your title here...")

# Theme template
ctk.set_appearance_mode("dark")  # or "light"
ctk.set_default_color_theme("dark-blue") # or "blue", "dark-blue", "green"

# Master frame
main_frame = ctk.CTkFrame(app).pack(expand = True, fill = BOTH)

app.mainloop()