from tkinter import *
import customtkinter as ctk
from ctk_temp_dual_frame import create_dual_frame
from ctk_temp_editable_list import create_editable_list

# Size templates
app = ctk.CTk()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height}+0+0")
app.update()
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

# Content of the frames
def sample_page(parent):
    frame = ctk.CTkFrame(parent, fg_color="transparent", corner_radius=0)
    create_editable_list(frame, columns=columns, data_list=sample_list, on_save=my_save_callback).pack(expand=True, fill=BOTH)
    return frame

frame_content = {
    "Sample": sample_page
}

# Make sure the background color are dark for better UI
# Either of the frame_content or frame_content_no_divider should work
dual_frame = create_dual_frame(app, frame_content, left_frame_bg_color="#000a35", right_frame_bg_color="#001545", button_hover_color="#1b285f")
dual_frame.pack(expand = True, fill = BOTH)

app.mainloop()