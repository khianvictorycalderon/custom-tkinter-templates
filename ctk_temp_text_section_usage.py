import customtkinter as ctk
from tkinter import *
from text_section import create_text_section
import webbrowser

app = ctk.CTk()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height}+0+0")
app.state("zoomed")

def sample_content_1(parent, text_color="white"):
    ctk.CTkLabel(parent, text="This is a sample content inside the text section.", text_color=text_color, anchor="w", justify="left").pack(fill="x")
    href = ctk.CTkLabel(parent, text="Developer", text_color="#3399ff", font=ctk.CTkFont(underline=True), cursor="hand2", anchor="w", justify="left")
    href.pack(fill="x")
    href.bind("<Button-1>", lambda _: webbrowser.open("https://khian.netlify.app/"))
    
def sample_content_2(parent, text_color="white"):
    ctk.CTkLabel(parent, text="This time, with another content and different horizontal rule color and background.", text_color=text_color, anchor="w", justify="left").pack(fill="x")

create_text_section(app, title="Welcome to the Text Section", content_fn=sample_content_1, text_color="white", bg_color="#003366").pack(fill=BOTH)
create_text_section(app, title="Another text section", content_fn=sample_content_2, text_color="white", bg_color="#205487", line_color="blue").pack(fill=BOTH)

app.mainloop()
