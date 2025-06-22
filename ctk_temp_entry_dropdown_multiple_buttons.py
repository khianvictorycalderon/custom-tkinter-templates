from tkinter import *
import customtkinter as ctk

def create_entry_dropdown_multiple_buttons(
        root,
        data,
        col_per_rows=1,
        label_color="white",
        input_bg_color="white",
        input_text_color="black",
        variable=None,
        buttons_color="Blue",
        buttons_hover_color="Blue",
        buttons=None,
        default_font=("Segoe UI", 13)
    ):
    content = ctk.CTkFrame(root, fg_color="transparent")
    content.grid_columnconfigure(tuple(range(col_per_rows)), weight=1)

    keys = list(data.keys())
    cols = [[] for _ in range(col_per_rows)]
    for i, key in enumerate(keys):
        cols[i % col_per_rows].append(key)

    # Measure label widths
    temp_labels = []
    max_label_widths = [0] * col_per_rows
    for col_index, col_keys in enumerate(cols):
        for key in col_keys:
            lbl = ctk.CTkLabel(content, text=key, text_color=label_color, font=default_font)
            lbl.pack_forget()
            temp_labels.append((col_index, lbl))

    root.update_idletasks()

    for col_index, lbl in temp_labels:
        w = lbl.winfo_reqwidth()
        if w > max_label_widths[col_index]:
            max_label_widths[col_index] = w

    for _, lbl in temp_labels:
        lbl.destroy()

    row = 0
    column = 0
    if variable is None:
        variable = {}

    for key, value in data.items():
        if column >= col_per_rows:
            column = 0
            row += 1

        input_frame = ctk.CTkFrame(content, fg_color="transparent")
        input_frame.grid(row=row, column=column, sticky="ew", padx=10, pady=5)
        input_frame.grid_columnconfigure(0, weight=0)
        input_frame.grid_columnconfigure(1, weight=1)

        label = ctk.CTkLabel(
            input_frame,
            text=f"{key}:",
            text_color=label_color,
            anchor="e",
            width=max_label_widths[column],
            font=default_font
        )
        label.grid(row=0, column=0, sticky="ew", padx=(0, 10))

        input_var = ctk.StringVar()
        if isinstance(value, list):
            input_var.set(value[0])
            input_widget = ctk.CTkOptionMenu(input_frame, variable=input_var, values=value, font=default_font,
                                             fg_color=input_bg_color, text_color=input_text_color, button_color=input_bg_color, button_hover_color=input_bg_color)
        elif value == "number":
            input_widget = ctk.CTkEntry(input_frame, fg_color=input_bg_color, font=default_font,
                                        text_color=input_text_color, textvariable=input_var)
            def validate_number(*args, var=input_var):
                val = var.get()
                if val == "" or val == "-":
                    return
                if val.startswith("-"):
                    var.set("-" + ''.join(filter(str.isdigit, val[1:])))
                else:
                    var.set(''.join(filter(str.isdigit, val)))
            input_var.trace_add("write", validate_number)

        elif value == "number_positive":
            input_widget = ctk.CTkEntry(input_frame, fg_color=input_bg_color, font=default_font,
                                        text_color=input_text_color, textvariable=input_var)
            def validate_positive(*args, var=input_var):
                var.set(''.join(filter(str.isdigit, var.get())))
            input_var.trace_add("write", validate_positive)

        elif value == "number_negative":
            input_widget = ctk.CTkEntry(input_frame, fg_color=input_bg_color, font=default_font,
                                        text_color=input_text_color, textvariable=input_var)
            def validate_negative(*args, var=input_var):
                val = var.get()
                if val == "" or val == "-":
                    return
                if not val.startswith("-"):
                    var.set("-" + ''.join(filter(str.isdigit, val)))
                else:
                    var.set("-" + ''.join(filter(str.isdigit, val[1:])))
            input_var.trace_add("write", validate_negative)

        elif value == "text_only":
            input_widget = ctk.CTkEntry(input_frame, fg_color=input_bg_color, font=default_font,
                                        text_color=input_text_color, textvariable=input_var)
            def validate_alpha(*args, var=input_var):
                var.set(''.join(filter(str.isalpha, var.get())))
            input_var.trace_add("write", validate_alpha)

        elif value == "password":
            input_widget = ctk.CTkEntry(input_frame, fg_color=input_bg_color, font=default_font,
                                        text_color=input_text_color, textvariable=input_var, show="*")
        else:
            input_widget = ctk.CTkEntry(input_frame, fg_color=input_bg_color, font=default_font,
                                        text_color=input_text_color, textvariable=input_var)

        input_widget.grid(row=0, column=1, sticky="ew")
        variable[key] = input_var
        column += 1

    # Button frame
    button_frame = ctk.CTkFrame(content, fg_color="transparent")
    button_frame.grid(row=row + 1, column=0, columnspan=col_per_rows, pady=10)

    if isinstance(buttons, dict):
        for btn_text, action in buttons.items():
            btn = ctk.CTkButton(button_frame, fg_color=buttons_color, hover_color=buttons_hover_color, text=btn_text, font=default_font, command=action)
            btn.pack(side=LEFT, padx=5)

    return content
