from tkinter import *
import customtkinter as ctk
from ctk_temp_dual_frame import create_dual_frame

# Size templates
app = ctk.CTk()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height}+0+0")
app.update()
app.state("zoomed")


# Content of the frames
def blog_page(parent):
    frame = ctk.CTkFrame(parent, fg_color="transparent", corner_radius=0)
    ctk.CTkLabel(frame, text="This is Blogs Page").pack(pady=5)
    ctk.CTkLabel(frame, text="Blog 1").pack(pady=5)
    ctk.CTkLabel(frame, text="Blog 2").pack(pady=5)
    ctk.CTkLabel(frame, text="And so on").pack(pady=5)
    return frame

def services_page(parent):
    frame = ctk.CTkFrame(parent, fg_color="transparent", corner_radius=0)
    ctk.CTkLabel(frame, text="This is Services Page").pack(pady=20)
    return frame

def products_page(parent):
    frame = ctk.CTkFrame(parent, fg_color="transparent", corner_radius=0)
    ctk.CTkLabel(frame, text="This is Products Page").pack(pady=20)
    return frame

def address_page(parent):
    frame = ctk.CTkFrame(parent, fg_color="transparent", corner_radius=0)
    ctk.CTkLabel(frame, text="This is Address Page").pack(pady=20)
    return frame

def phone_page(parent):
    frame = ctk.CTkFrame(parent, fg_color="transparent", corner_radius=0)
    ctk.CTkLabel(frame, text="This is Phone Number Page").pack(pady=20)
    return frame

def email_page(parent):
    frame = ctk.CTkFrame(parent, fg_color="transparent", corner_radius=0)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    ctk.CTkLabel(frame, text="This is Email Page").pack(pady=20)
    return frame

frame_content = {
    "Home": {
        "Blogs": blog_page,
        "Services": services_page,
        "Products": products_page,
    },
    "Contact": {
        "Address": address_page,
        "Phone Number": phone_page,
        "Email": email_page,
    }
}

frame_content_no_divider = {
    "Blogs": blog_page,
    "Services": services_page,
    "Products": products_page,
    "Address": address_page,
    "Phone Number": phone_page,
    "Email": email_page
}

# Make sure the background color are dark for better UI
# Either of the frame_content or frame_content_no_divider should work
dual_frame = create_dual_frame(app, frame_content, left_frame_bg_color="#000a35", right_frame_bg_color="#001545", button_hover_color="#1b285f")
dual_frame.pack(expand = True, fill = BOTH)

app.mainloop()