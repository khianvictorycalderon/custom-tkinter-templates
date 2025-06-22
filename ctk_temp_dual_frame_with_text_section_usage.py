from tkinter import *
import customtkinter as ctk
from ctk_temp_dual_frame import create_dual_frame
from ctk_temp_text_section import create_text_section

# Size templates
app = ctk.CTk()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height}+0+0")
app.update()
app.state("zoomed")

# Content of the frames
def create_content(parent, text_color="white"):
    ctk.CTkLabel(parent, text="Text section integrated with dual frame.", text_color=text_color, anchor="w", justify="left").pack(fill="x")
    
def flex_text_container(parent):
    frame = ctk.CTkFrame(parent, fg_color="transparent", corner_radius=0)
    create_text_section(frame, title="Sample Title", content_fn=create_content, bg_color="#45002C").pack(fill = BOTH)
    return frame

frame_content = {
    "Sample": flex_text_container
}

# Make sure the background color are dark for better UI
# Either of the frame_content or frame_content_no_divider should work
dual_frame = create_dual_frame(app, frame_content, left_frame_bg_color="#320035", right_frame_bg_color="#45002C", button_hover_color="#5f1b56")
dual_frame.pack(expand = True, fill = BOTH)

app.mainloop()