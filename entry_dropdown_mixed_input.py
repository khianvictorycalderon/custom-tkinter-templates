from tkinter import *
import customtkinter as ctk

def create_entry_dropdown(root, data, col_per_rows=1, label_color="white", input_bg_color="", input_text_color="", variable=None):
    # Create and pack a temp frame to measure width
    temp = ctk.CTkFrame(root)
    temp.pack(fill="both", expand=True)
    root.update_idletasks()

    total_width = temp.winfo_width() or root.winfo_width()
    temp.destroy()

    column_width = total_width // col_per_rows
    label_width = int(column_width * (1/5))
    input_width = int(column_width * (4/5))

    content = ctk.CTkFrame(root, fg_color="transparent")
    content.grid_columnconfigure(tuple(range(col_per_rows)), weight=1)

    row = 0
    column = 0
    widgets = {}

    if variable is None:
        variable = {}

    for key, value in data.items():
        if column >= col_per_rows:
            column = 0
            row += 1

        input_frame = ctk.CTkFrame(content, fg_color="transparent", width=column_width)
        input_frame.grid(row=row, column=column, sticky="nsew", padx=10, pady=5)

        label = ctk.CTkLabel(input_frame, text=key, text_color=label_color, anchor="e", width=label_width)
        label.pack(side="left", padx=(0, 10))

        # Create StringVar here for entries and comboboxes as needed
        if isinstance(value, list):
            # Combobox (OptionMenu)
            input_var = ctk.StringVar(value=value[0])
            input_widget = ctk.CTkOptionMenu(input_frame, variable=input_var, values=value,
                                            fg_color=input_bg_color, text_color=input_text_color, width=input_width)

        elif value == "number":
            input_var = ctk.StringVar()
            input_widget = ctk.CTkEntry(input_frame, fg_color=input_bg_color, text_color=input_text_color,
                                        width=input_width, textvariable=input_var)

            def validate_number(*args, var=input_var):
                val = var.get()
                if val == "":
                    return
                if val == "-":
                    return
                if val.startswith("-"):
                    if not val[1:].isdigit():
                        new_val = "-" + ''.join(filter(str.isdigit, val[1:]))
                        var.set(new_val)
                else:
                    if not val.isdigit():
                        new_val = ''.join(filter(str.isdigit, val))
                        var.set(new_val)

            input_var.trace_add("write", validate_number)

        elif value == "number_positive":
            input_var = ctk.StringVar()
            input_widget = ctk.CTkEntry(input_frame, fg_color=input_bg_color, text_color=input_text_color,
                                        width=input_width, textvariable=input_var)

            def validate_positive_number(*args, var=input_var):
                val = var.get()
                if val == "":
                    return
                if not val.isdigit():
                    new_val = ''.join(filter(str.isdigit, val))
                    var.set(new_val)

            input_var.trace_add("write", validate_positive_number)

        elif value == "number_negative":
            input_var = ctk.StringVar()
            input_widget = ctk.CTkEntry(input_frame, fg_color=input_bg_color, text_color=input_text_color,
                                        width=input_width, textvariable=input_var)

            def validate_negative_number(*args, var=input_var):
                val = var.get()
                if val == "":
                    return
                if val == "-":
                    return
                if not val.startswith("-"):
                    new_val = "-" + ''.join(filter(str.isdigit, val))
                    var.set(new_val)
                else:
                    if not val[1:].isdigit():
                        new_val = "-" + ''.join(filter(str.isdigit, val[1:]))
                        var.set(new_val)

            input_var.trace_add("write", validate_negative_number)

        elif value == "text_only":
            input_var = ctk.StringVar()
            input_widget = ctk.CTkEntry(input_frame, fg_color=input_bg_color, text_color=input_text_color,
                                        width=input_width, textvariable=input_var)

            def validate_text_only(*args, var=input_var):
                val = var.get()
                if val == "":
                    return
                new_val = ''.join(filter(lambda c: c.isalpha(), val))
                if val != new_val:
                    var.set(new_val)

            input_var.trace_add("write", validate_text_only)

        elif value == "text":
            input_var = ctk.StringVar()
            input_widget = ctk.CTkEntry(input_frame, fg_color=input_bg_color, text_color=input_text_color,
                                        width=input_width, textvariable=input_var)

        else:
            # fallback to normal entry
            input_var = ctk.StringVar()
            input_widget = ctk.CTkEntry(input_frame, fg_color=input_bg_color, text_color=input_text_color,
                                        width=input_width, textvariable=input_var)

        input_widget.pack(side="left", fill="x")
        widgets[key] = input_widget
        variable[key] = input_var  # STORE the StringVar here!

        column += 1

    return content