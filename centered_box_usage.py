from tkinter import *
import customtkinter as ctk
from centered_box import create_centered_box

# Size templates
app = ctk.CTk()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height}+0+0")
app.update()
app.state("zoomed")

def box_content(frame):
    ctk.CTkLabel(frame, text="Welcome!", text_color="white", fg_color="transparent").pack()
    ctk.CTkButton(frame, text="Click Me").pack(pady=10)

centered_box = create_centered_box(app, bg_color="black", box_bg_color="gray", text_color="white", content_fn=box_content)
centered_box.pack(expand = True, fill = BOTH)

app.mainloop()