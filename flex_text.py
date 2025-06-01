import customtkinter as ctk
from PIL import Image, ImageTk
import os

def create_flex_text(
        root, 
        data, 
        bg_color="#041c40", 
        text_color="white", 
        title_font=("Segoe UI", 18), 
        subtitle_font=("Segoe UI", 13)
    ):
    
    container = ctk.CTkFrame(root, corner_radius=0, fg_color=bg_color)

    # === Logos row on top ===
    logos = data.get("logo", [])
    if logos:
        logos_frame = ctk.CTkFrame(container, fg_color="transparent")
        logos_frame.pack(fill="x", pady=(0, 20))

        for logo_file in logos:
            if os.path.exists(logo_file):
                img = Image.open(logo_file)
                img = img.resize((80, 30), Image.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                label = ctk.CTkLabel(logos_frame, image=photo, text="", fg_color="transparent")
                label.image = photo  # keep reference
                label.pack(side="left", padx=10)
            else:
                ctk.CTkLabel(logos_frame, text=f"[Missing Image: {logo_file}]",
                             text_color=text_color, font=subtitle_font).pack(side="left", padx=10)

    # === Text sections row below logos ===
    text_keys = [k for k in data.keys() if k != "logo"]
    text_sections_frame = ctk.CTkFrame(container, fg_color="transparent")
    text_sections_frame.pack(fill="x")

    for key in text_keys:
        section_data = data[key]
        section_frame = ctk.CTkFrame(text_sections_frame, fg_color="transparent")
        section_frame.pack(side="left", padx=30, expand=True, fill="both")

        # Section Title (Apply title_font)
        ctk.CTkLabel(section_frame, text=key.upper(), text_color=text_color,
                     font=title_font, anchor="w").pack(anchor="w", pady=(0, 8))

        # Detect if section_data is a list of lists
        is_list_of_lists = (
            isinstance(section_data, list) and
            len(section_data) > 0 and
            all(isinstance(i, (list, tuple)) for i in section_data)
        )

        if is_list_of_lists:
            columns_frame = ctk.CTkFrame(section_frame, fg_color="transparent")
            columns_frame.pack(fill="x")

            for col_items in section_data:
                col_frame = ctk.CTkFrame(columns_frame, fg_color="transparent")
                col_frame.pack(side="left", padx=15, anchor="n")

                for item in col_items:
                    ctk.CTkLabel(col_frame, text=str(item), text_color=text_color,
                                 font=subtitle_font, anchor="w").pack(anchor="w")
        else:
            for item in section_data:
                ctk.CTkLabel(section_frame, text=str(item), text_color=text_color,
                             font=subtitle_font, anchor="w").pack(anchor="w")

    return container
