from tkinter import *
import customtkinter as ctk
from dual_frame import create_dual_frame
from editable_list import create_editable_list, ArrayVar

# Size templates
app = ctk.CTk()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height}+0+0")
app.update()
app.state("zoomed")

sample_list = ArrayVar(value=[
    ["John", 17, "Brook Street"],
    ["Jake", 18, "Venezuela"],
    ["Paul", 21, "Russia"],
    ["Jane", 16, "United States"]
])

headers = ["Name", "Last Name", "Address 1"]

def my_save_callback(data):
    for row in data:
        print(row, ",")

# Content of the frames
def sample_page(parent):
    frame = ctk.CTkFrame(parent, fg_color="transparent", corner_radius=0)
    create_editable_list(frame, headers=headers, data_var=sample_list, column_per_rows=3, on_save=my_save_callback).pack(expand=True, fill=BOTH)
    return frame

frame_content = {
    "Sample": sample_page
}

# Make sure the background color are dark for better UI
# Either of the frame_content or frame_content_no_divider should work
dual_frame = create_dual_frame(app, frame_content, left_frame_bg_color="#000a35", right_frame_bg_color="#001545", button_hover_color="#1b285f")
dual_frame.pack(expand = True, fill = BOTH)

app.mainloop()