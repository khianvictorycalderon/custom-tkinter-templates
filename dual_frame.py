import customtkinter as ctk
from tkinter import *

def create_dual_frame(
        root, 
        nav_dict, 
        left_frame_bg_color="#2e2e2e", 
        right_frame_bg_color="#3F3F3F", 
        button_hover_color="blue", 
        text_color="white", 
        left_ratio=0.2,
        left_frame_font=("Segoe UI", 13) # Default for all Windows
    ):
    content = ctk.CTkFrame(root)

    left_frame = ctk.CTkScrollableFrame(content, fg_color=left_frame_bg_color, corner_radius=0)
    left_frame.pack(side="left", fill="y")

    right_frame = ctk.CTkScrollableFrame(content, fg_color=right_frame_bg_color, corner_radius=0)
    right_frame.pack(side="right", fill="both", expand=True)

    def clear_right_frame():
        for widget in right_frame.winfo_children():
            widget.destroy()

    def show_content(content_fn):
        clear_right_frame()
        result = content_fn(right_frame)
        if isinstance(result, ctk.CTkBaseClass) or hasattr(result, "pack"):
            result.pack(fill="both", expand=True)

    def on_resize(event):
        new_width = event.width
        left_frame_width = int(new_width * left_ratio)
        left_frame.configure(width=left_frame_width)

    content.bind("<Configure>", on_resize)

    is_flat = all(callable(v) for v in nav_dict.values())

    if is_flat:
        for btn_label, content_fn in nav_dict.items():
            def handler(fn=content_fn):
                show_content(fn)
            btn = ctk.CTkButton(
                left_frame,
                text=btn_label,
                font=left_frame_font,
                fg_color=left_frame_bg_color,
                text_color=text_color,
                hover=True,
                hover_color=button_hover_color,
                command=handler
            )
            btn.pack(fill="x", padx=20, pady=2)
    else:
        for section, buttons in nav_dict.items():
            section_title = ctk.CTkLabel(
                left_frame,
                text=section,
                font=ctk.CTkFont(family=left_frame_font[0], size=left_frame_font[1], weight="bold"),
                text_color=text_color,
                fg_color=left_frame_bg_color,
                anchor="center"
            )
            section_title.pack(fill="x", padx=10, pady=(20, 0))

            divider = ctk.CTkFrame(left_frame, height=2, fg_color="#AAAAAA")
            divider.pack(fill="x", padx=10, pady=(2, 6))

            for btn_label, content_fn in buttons.items():
                def handler(fn=content_fn):
                    show_content(fn)
                btn = ctk.CTkButton(
                    left_frame,
                    text=btn_label,
                    font=left_frame_font,
                    fg_color=left_frame_bg_color,
                    text_color=text_color,
                    hover=True,
                    hover_color=button_hover_color,
                    command=handler
                )
                btn.pack(fill="x", padx=20, pady=2)

    if is_flat:
        first_fn = next(iter(nav_dict.values()))
        show_content(first_fn)
    else:
        for section_buttons in nav_dict.values():
            if section_buttons:
                first_fn = next(iter(section_buttons.values()))
                show_content(first_fn)
                break

    return content