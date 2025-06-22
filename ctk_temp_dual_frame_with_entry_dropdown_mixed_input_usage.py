from tkinter import *
import customtkinter as ctk
from dual_frame import create_dual_frame
from entry_dropdown_mixed_input import create_entry_dropdown

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
def sample_page(parent):
    frame = ctk.CTkFrame(parent, fg_color="transparent", corner_radius=0)
    
    def print_all_values():
        for key, var in input_vars.items():
            print(f"{key}: {var.get()}")
    
    create_entry_dropdown(
        frame, 
        input_fields, 
        col_per_rows=2, 
        input_bg_color="#CBE5F7",
        input_text_color="#151D41",
        variable=input_vars,
        button_label="Print all data",
        on_submit=print_all_values
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