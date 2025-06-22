import customtkinter as ctk
from tkinter import *

def create_text_section(
        root, 
        title="Title", 
        content_fn=None, 
        text_color="white", 
        bg_color="blue", 
        line_color="#AAAAAA",
        title_font=("Segoe UI", 18)
    ):
    content = ctk.CTkFrame(root, fg_color=bg_color, corner_radius=0)
    
    # Title label (aligned left)
    title_label = ctk.CTkLabel(
        content,
        text=title,
        text_color=text_color,
        font=title_font,
        anchor="w"
    )
    title_label.pack(fill="x", padx=20, pady=(20, 5))
    
    # Horizontal line (divider)
    hr = ctk.CTkFrame(content, height=2, fg_color=line_color)
    hr.pack(fill="x", padx=20, pady=(0, 5))
    
    # Content area frame
    content_frame = ctk.CTkFrame(content, fg_color="transparent")
    content_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
    
    # If a content function is passed, call it with content_frame as parent
    if content_fn:
        content_fn(content_frame, text_color=text_color)
    
    return content