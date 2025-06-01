from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import re

def create_entry_dropdown(
        root, 
        data, 
        col_per_rows=1, 
        label_color="white", 
        input_bg_color="", 
        input_text_color="", 
        variable=None, 
        button_label="submit",
        on_submit=None,
        default_font=("Segoe UI", 13)
    ):
    content = ctk.CTkFrame(root, fg_color="transparent")
    content.grid_columnconfigure(tuple(range(col_per_rows)), weight=1)

    # Split keys by columns
    keys = list(data.keys())
    cols = [[] for _ in range(col_per_rows)]
    for i, key in enumerate(keys):
        cols[i % col_per_rows].append(key)

    # Measure max label widths per column
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
    widgets = {}
    if variable is None:
        variable = {}

    for key, value in data.items():
        if column >= col_per_rows:
            column = 0
            row += 1

        input_frame = ctk.CTkFrame(content, fg_color="transparent")
        input_frame.grid(row=row, column=column, sticky="ew", padx=10, pady=5)
        input_frame.grid_columnconfigure(0, weight=0)  # fixed label width
        input_frame.grid_columnconfigure(1, weight=1)  # input expands

        label = ctk.CTkLabel(
            input_frame, 
            text=key, 
            text_color=label_color, 
            anchor="e", 
            width=max_label_widths[column], 
            font=default_font
        )
        label.grid(row=0, column=0, sticky="ew", padx=(0, 10))

        if isinstance(value, list):
            input_var = ctk.StringVar(value=value[0])
            input_widget = ctk.CTkOptionMenu(input_frame, variable=input_var, values=value, font=default_font,
                                            fg_color=input_bg_color, text_color=input_text_color)
        elif value == "number":
            input_var = ctk.StringVar()
            input_widget = ctk.CTkEntry(input_frame, fg_color=input_bg_color, font=default_font,
                                        text_color=input_text_color, textvariable=input_var)

            def validate_number(*args, var=input_var):
                val = var.get()
                if val == "" or val == "-":
                    return
                if val.startswith("-"):
                    if not val[1:].isdigit():
                        var.set("-" + ''.join(filter(str.isdigit, val[1:])))
                else:
                    if not val.isdigit():
                        var.set(''.join(filter(str.isdigit, val)))

            input_var.trace_add("write", validate_number)

        elif value == "number_positive":
            input_var = ctk.StringVar()
            input_widget = ctk.CTkEntry(input_frame, fg_color=input_bg_color, font=default_font,
                                        text_color=input_text_color, textvariable=input_var)

            def validate_positive_number(*args, var=input_var):
                val = var.get()
                if val == "":
                    return
                if not val.isdigit():
                    var.set(''.join(filter(str.isdigit, val)))

            input_var.trace_add("write", validate_positive_number)

        elif value == "number_negative":
            input_var = ctk.StringVar()
            input_widget = ctk.CTkEntry(input_frame, fg_color=input_bg_color, font=default_font,
                                        text_color=input_text_color, textvariable=input_var)

            def validate_negative_number(*args, var=input_var):
                val = var.get()
                if val == "" or val == "-":
                    return
                if not val.startswith("-"):
                    var.set("-" + ''.join(filter(str.isdigit, val)))
                else:
                    if not val[1:].isdigit():
                        var.set("-" + ''.join(filter(str.isdigit, val[1:])))

            input_var.trace_add("write", validate_negative_number)

        elif value == "text_only":
            input_var = ctk.StringVar()
            input_widget = ctk.CTkEntry(input_frame, fg_color=input_bg_color, font=default_font,
                                        text_color=input_text_color, textvariable=input_var)

            def validate_text_only(*args, var=input_var):
                val = var.get()
                if val == "":
                    return
                new_val = ''.join(filter(str.isalpha, val))
                if val != new_val:
                    var.set(new_val)

            input_var.trace_add("write", validate_text_only)

        elif value == "text":
            input_var = ctk.StringVar()
            input_widget = ctk.CTkEntry(input_frame, fg_color=input_bg_color, font=default_font,
                                        text_color=input_text_color, textvariable=input_var)

        else:
            input_var = ctk.StringVar()
            input_widget = ctk.CTkEntry(input_frame, fg_color=input_bg_color, font=default_font,
                                        text_color=input_text_color, textvariable=input_var)

        input_widget.grid(row=0, column=1, sticky="ew")

        widgets[key] = input_widget
        variable[key] = input_var

        column += 1

    def internal_on_submit():
        empty_fields = [key for key, var in variable.items() if var.get().strip() == ""]
        if empty_fields:
            messagebox.showerror(
                "Validation Error", 
                f"The following fields must not be empty:\n- " + "\n- ".join(empty_fields)
            )
            return

        # Email validation regex (simple)
        email_pattern = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

        # Check all email fields
        invalid_emails = []
        for key, value_type in data.items():
            if value_type == "email":
                email_val = variable[key].get().strip()
                if not email_pattern.match(email_val):
                    invalid_emails.append(key)

        if invalid_emails:
            messagebox.showerror(
                "Validation Error", 
                f"The following email fields are invalid:\n- " + "\n- ".join(invalid_emails)
            )
            return

        if on_submit is not None:
            on_submit()

    submit_button = ctk.CTkButton(content, text=button_label,  font=default_font, command=internal_on_submit)
    submit_button.grid(row=row + 1, column=0, columnspan=col_per_rows, pady=10)

    return content
