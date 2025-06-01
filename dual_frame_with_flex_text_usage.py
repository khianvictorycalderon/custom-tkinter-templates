from tkinter import *
import customtkinter as ctk
from dual_frame import create_dual_frame
from flex_text import create_flex_text

# Size templates
app = ctk.CTk()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height}+0+0")
app.update()
app.state("zoomed")

sample_data = {
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
    ]
}

# Content of the frames
def flex_text_container(parent):
    frame = ctk.CTkFrame(parent, fg_color="transparent", corner_radius=0)
    create_flex_text(frame, sample_data, bg_color="#004507").pack(fill = BOTH)
    return frame

frame_content = {
    "Sample": flex_text_container
}

# Make sure the background color are dark for better UI
# Either of the frame_content or frame_content_no_divider should work
dual_frame = create_dual_frame(app, frame_content, left_frame_bg_color="#00350a", right_frame_bg_color="#004507", button_hover_color="#1c5f1b")
dual_frame.pack(expand = True, fill = BOTH)

app.mainloop()