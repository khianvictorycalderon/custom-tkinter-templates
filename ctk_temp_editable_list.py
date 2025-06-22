import customtkinter as ctk
import tkinter as tk

def is_valid_number(value, allow_negative=True, allow_positive=True):
    if value in ("", "-", "."):
        return True
    try:
        num = float(value)
        if not allow_negative and num < 0:
            return False
        if not allow_positive and num > 0:
            return False
        return True
    except ValueError:
        return False

def create_editable_list(
        root,
        columns,  # No need to set column per rows
        data_list,  # Now using a regular list
        font=("Segoe UI", 13),
        content_bg="#292929",
        input_bg_color="#FFFFFF",
        input_text_color="#000000",
        headers_text_color="white",
        on_save=None,
    ):
    container = ctk.CTkFrame(root, fg_color=content_bg, corner_radius=0)
    original_data = []

    rows = []
    editing = tk.BooleanVar(value=False)
    headers = list(columns.keys())

    for col in range(len(headers)):
        container.grid_columnconfigure(col, weight=1)
    container.grid_columnconfigure(len(headers), weight=0)

    buttons_frame = ctk.CTkFrame(container, fg_color=content_bg)
    buttons_frame.grid_columnconfigure(0, weight=1)
    buttons_frame.grid_columnconfigure(1, weight=1)

    for col_index, header in enumerate(headers):
        ctk.CTkLabel(
            container,
            text=header,
            text_color=headers_text_color,
            font=font,
            anchor="w"
        ).grid(row=0, column=col_index, padx=(10 if col_index == 0 else 5, 5), pady=(10, 5), sticky="w")
    ctk.CTkLabel(container, text="", fg_color=content_bg).grid(row=0, column=len(headers), padx=(5, 10), pady=(10, 5))

    def refresh_list():
        for row in rows:
            for widget in row["widgets"]:
                widget.destroy()
        rows.clear()

        for i, row_vals in enumerate(data_list):
            add_row(row_vals, index=i)

        if editing.get():
            add_row([""] * len(headers), index=len(data_list), is_new=True)

    def validate_input(entry, col_type):
        def handler(P):
            if col_type == "number":
                return is_valid_number(P)
            elif col_type == "number_positive":
                return is_valid_number(P, allow_negative=False)
            elif col_type == "number_negative":
                return is_valid_number(P, allow_positive=False)
            return True
        return handler

    def add_row(values, index=None, is_new=False):
        widgets = []
        entries = []

        for col_index, (col_name, col_type) in enumerate(columns.items()):
            val = values[col_index] if col_index < len(values) else ""

            if isinstance(col_type, list):
                if editing.get():
                    # Editable dropdown option menu
                    entry = ctk.CTkOptionMenu(
                        container,
                        values=col_type,
                        font=font,
                        fg_color=input_bg_color,
                        text_color=input_text_color,
                        button_color=input_bg_color,
                        button_hover_color=input_bg_color,
                    )
                    entry.set(val)
                else:
                    # Non-editable display: readonly CTkEntry showing the value with StringVar
                    var = tk.StringVar(value=val)
                    entry = ctk.CTkEntry(
                        container,
                        width=150,
                        fg_color=input_bg_color,
                        text_color=input_text_color,
                        font=font,
                        corner_radius=6,
                        border_width=1,
                        border_color="#cccccc",
                        textvariable=var,
                        state="readonly"
                    )
            else:
                # Normal entry (text or number)
                entry = ctk.CTkEntry(
                    container,
                    width=150,
                    fg_color=input_bg_color,
                    text_color=input_text_color,
                    font=font,
                    corner_radius=6,
                    border_width=1,
                    border_color="#cccccc"
                )
                if editing.get():
                    entry.insert(0, val)
                    if col_type.startswith("number"):
                        vcmd = container.register(validate_input(entry, col_type))
                        entry.configure(validate="key", validatecommand=(vcmd, "%P"))
                else:
                    # Non-edit mode readonly with StringVar for display
                    var = tk.StringVar(value=val)
                    entry.configure(state="readonly", textvariable=var)

            entry.grid(row=index + 1, column=col_index, padx=(10 if col_index == 0 else 5, 5), pady=5, sticky="ew")
            if editing.get():
                entry.bind("<KeyRelease>", on_change)
            entries.append(entry)
            widgets.append(entry)

        delete_btn = ctk.CTkButton(
            container,
            text="Delete",
            width=80,
            fg_color="#dc3545",
            hover_color="#c82333",
            text_color="#ffffff",
            font=font,
            corner_radius=6,
            command=lambda r=len(rows): delete_row_by_row_index(r)
        )
        delete_btn.grid(row=index + 1, column=len(headers), padx=(5, 10), pady=5, sticky="ew")
        if not editing.get() or is_new:
            delete_btn.grid_remove()
        widgets.append(delete_btn)

        rows.append({"widgets": widgets, "entries": entries, "is_new": is_new})

    def on_change(event=None):
        if not editing.get():
            return
        for row in rows:
            if row.get("is_new"):
                has_content = any(entry.get().strip() for entry in row["entries"])
                if has_content:
                    row["is_new"] = False
                    row["widgets"][-1].grid()
                    add_row([""] * len(headers), index=len(rows), is_new=True)
                    break
                else:
                    row["widgets"][-1].grid_remove()

    def delete_row_by_row_index(row_index):
        if row_index >= len(rows):
            return
        row = rows[row_index]
        if row["is_new"]:
            return
        if row_index < len(data_list):
            data_list.pop(row_index)
            refresh_list()

    def enable_edit():
        original_data.clear()
        original_data.extend([r[:] for r in data_list])
        editing.set(True)
        refresh_list()
        edit_btn.grid_forget()
        save_btn.grid(row=999, column=0, padx=10, pady=10, sticky="ew")
        cancel_btn.grid(row=999, column=1, padx=10, pady=10, sticky="ew")

    def save_changes():
        values = []
        for row in rows:
            row_values = []
            for entry in row["entries"]:
                # If it's an OptionMenu, use .get(), else Entry .get()
                if isinstance(entry, ctk.CTkOptionMenu):
                    row_values.append(entry.get())
                else:
                    row_values.append(entry.get())
            if any(row_values):
                values.append(row_values)
        data_list.clear()
        data_list.extend(values)
        if on_save is not None:
            on_save(values)
        editing.set(False)
        refresh_list()
        save_btn.grid_forget()
        cancel_btn.grid_forget()
        edit_btn.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    def cancel_changes():
        data_list.clear()
        data_list.extend([r[:] for r in original_data])
        editing.set(False)
        refresh_list()
        save_btn.grid_forget()
        cancel_btn.grid_forget()
        edit_btn.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    edit_btn = ctk.CTkButton(buttons_frame, text="Edit", command=enable_edit, fg_color="#28a745", hover_color="#218838", text_color="#ffffff", font=font, corner_radius=6)
    save_btn = ctk.CTkButton(buttons_frame, text="Save", command=save_changes, fg_color="#007bff", hover_color="#0069d9", text_color="#ffffff", font=font, corner_radius=6)
    cancel_btn = ctk.CTkButton(buttons_frame, text="Cancel", command=cancel_changes, fg_color="#6c757d", hover_color="#5a6268", text_color="#ffffff", font=font, corner_radius=6)

    refresh_list()

    buttons_frame.grid(row=999, column=0, columnspan=len(headers) + 1, sticky="ew")
    edit_btn.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    return container