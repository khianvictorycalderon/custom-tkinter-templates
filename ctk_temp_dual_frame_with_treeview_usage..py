from tkinter import *
import customtkinter as ctk
from ctk_temp_dual_frame import create_dual_frame
from ctk_temp_treeview import create_treeview

# Size templates
app = ctk.CTk()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height}+0+0")
app.update()
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

# Content of the frames
def sample_page(parent):
    def copy_id(data):
        print("Copy ID:", data[0])  # first column of the row

    def delete_item(data):
        print("Delete:", data)

    buttons = {
        "Copy ID": {
            "📜": copy_id
        },
        "Delete Item": {
            "⛔": delete_item
        }
    }
    
    frame = ctk.CTkFrame(parent, fg_color="transparent", corner_radius=0)
    create_treeview(frame, action_buttons=buttons, columns=sample_columns, data=sample_data, column_width=700, alternate_row_bg=False).pack(fill = BOTH)
    return frame

frame_content = {
    "Home": sample_page
}

# Make sure the background color are dark for better UI
# Either of the frame_content or frame_content_no_divider should work
dual_frame = create_dual_frame(app, frame_content, left_frame_bg_color="#000a35", right_frame_bg_color="#001545", button_hover_color="#1b285f")
dual_frame.pack(expand = True, fill = BOTH)

app.mainloop()