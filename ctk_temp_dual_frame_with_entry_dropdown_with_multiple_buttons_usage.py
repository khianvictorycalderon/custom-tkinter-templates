from tkinter import *
import customtkinter as ctk
from tkinter import messagebox
from ctk_temp_dual_frame import create_dual_frame
from ctk_temp_entry_dropdown_multiple_buttons import create_entry_dropdown_multiple_buttons

# Size templates
app = ctk.CTk()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height}+0+0")
app.update()
app.state("zoomed")

input_vars = {}
input_fields = {
    "Name": "text_only",
    "Age":  "number",
    "Email": "email",
    "Type": ["Excellent", "Good", "Fair"],
    "Agenda": "text",
    "Blah Blah": "number",
    "SKAFIASKFOSKFOASKOFA": "text",
    "Department": ["Department 1", "Department 2"],
    "Gender": ["Male", "Female"]
}

# Content of the frames

variables = {}

def add_action():
    values = {k: v.get() for k, v in variables.items()}
    print("Add clicked:", values)
    messagebox.showinfo("Add", f"Added:\n{values}")

def edit_action():
    values = {k: v.get() for k, v in variables.items()}
    print("Edit clicked:", values)
    messagebox.showinfo("Edit", f"Edited:\n{values}")

def remove_action():
    values = {k: v.get() for k, v in variables.items()}
    print("Remove clicked:", values)
    messagebox.showinfo("Remove", f"Removed:\n{values}")

data = {
    "Name": "text_only",
    "Email": "email",
    "Age": "number_positive",
    "Gender": ["Male", "Female", "Other"]
}

buttons = {
    "Add": add_action,
    "Edit": edit_action,
    "Remove": remove_action
}

def sample_page(parent):
    frame = ctk.CTkFrame(parent, fg_color="transparent", corner_radius=0)
    
    create_entry_dropdown_multiple_buttons(
        root=frame,
        data=data,
        col_per_rows=2,
        variable=variables,
        buttons=buttons,
        label_color="white",
        input_bg_color="#f0f0f0",
        input_text_color="black"
    ).pack(fill = BOTH, expand = True)
    
    return frame

frame_content = {
    "Home": sample_page
}

# Make sure the background color are dark for better UI
# Either of the frame_content or frame_content_no_divider should work
dual_frame = create_dual_frame(app, frame_content, left_frame_bg_color="#000a35", right_frame_bg_color="#001545", button_hover_color="#1b285f")
dual_frame.pack(expand = True, fill = "both")

app.mainloop()