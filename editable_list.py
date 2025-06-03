import customtkinter as ctk
import tkinter as tk

class ArrayVar(tk.Variable):
    def __init__(self, master=None, value=None, name=None):
        value = value if value is not None else []
        super().__init__(master, name)
        self.set(value)

    def get(self):
        val = super().get()
        if not val:
            return []
        rows = val.split(";")
        result = []
        for row in rows:
            if row.strip():
                cols = row.split(",")
                result.append(cols)
        return result

    def set(self, value):
        if isinstance(value, list):
            flattened = []
            for row in value:
                str_row = [str(col) for col in row]
                flattened.append(",".join(str_row))
            value = ";".join(flattened)
        super().set(value)

def create_editable_list(
        root,
        headers,
        data_var: ArrayVar,
        column_per_rows=1,
        font=("Segoe UI", 13),
        content_bg="#292929",
        entry_bg_color="#FFFFFF",
        entry_text_color="#000000",
        headers_text_color="white",
        on_save=None,
    ):
    container = ctk.CTkFrame(root, fg_color=content_bg, corner_radius=0)
    original_data = []

    for col in range(column_per_rows):
        container.grid_columnconfigure(col, weight=1)
    container.grid_columnconfigure(column_per_rows, weight=0)

    rows = []
    editing = tk.BooleanVar(value=False)

    buttons_frame = ctk.CTkFrame(container, fg_color=content_bg)
    buttons_frame.grid_columnconfigure(0, weight=1)
    buttons_frame.grid_columnconfigure(1, weight=1)

    # Add headers above the editable rows
    for col_index, header in enumerate(headers):
        header_label = ctk.CTkLabel(
            container,
            text=header,
            text_color=headers_text_color,
            font=font,
            anchor="w"
        )
        header_label.grid(row=0, column=col_index, padx=(10 if col_index == 0 else 5, 5), pady=(10, 5), sticky="w")
    ctk.CTkLabel(container, text="", fg_color=content_bg).grid(row=0, column=column_per_rows, padx=(5, 10), pady=(10, 5))

    def refresh_list():
        for row in rows:
            for entry in row["entries"]:
                entry.destroy()
            row["delete"].destroy()
        rows.clear()

        values = data_var.get()

        for i, row_vals in enumerate(values):
            add_row(row_vals, index=i)

        if editing.get():
            add_row([""] * column_per_rows, index=len(values), is_new=True)

    def on_change(event=None):
        if not editing.get():
            return

        for row in rows:
            if row.get("is_new"):
                has_content = any(entry.get().strip() for entry in row["entries"])
                if has_content:
                    row["is_new"] = False
                    row["delete"].grid()
                    add_row([""] * column_per_rows, index=len(rows), is_new=True)
                    break
                else:
                    row["delete"].grid_remove()

    def add_row(values, index=None, is_new=False):
        entries = []
        for col in range(column_per_rows):
            entry = ctk.CTkEntry(
                container,
                width=150,
                fg_color=entry_bg_color,
                text_color=entry_text_color,
                font=font,
                corner_radius=6,
                border_width=1,
                border_color="#cccccc"
            )
            try:
                entry.insert(0, values[col])
            except IndexError:
                entry.insert(0, "")
            if not editing.get() and not is_new:
                entry.configure(state="readonly")
            entry.grid(row=index + 1, column=col, padx=(10 if col == 0 else 5, 5), pady=5, sticky="ew")
            entry.bind("<KeyRelease>", on_change)
            entries.append(entry)

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
        delete_btn.grid(row=index + 1, column=column_per_rows, padx=(5, 10), pady=5, sticky="ew")
        if not editing.get() or is_new:
            delete_btn.grid_remove()

        rows.append({
            "entries": entries,
            "delete": delete_btn,
            "is_new": is_new,
        })

    def delete_row_by_row_index(row_index):
        if row_index >= len(rows):
            return

        row = rows[row_index]

        if row["is_new"]:
            return

        if editing.get():
            if row_index >= len(data_var.get()):
                for entry in row["entries"]:
                    entry.destroy()
                row["delete"].destroy()
                rows.pop(row_index)
                for i in range(row_index, len(rows)):
                    for j, entry in enumerate(rows[i]["entries"]):
                        entry.grid(row=i + 1, column=j)
                    rows[i]["delete"].grid(row=i + 1, column=column_per_rows)
            else:
                current = data_var.get()
                current.pop(row_index)
                data_var.set(current)
                refresh_list()

    def enable_edit():
        original_data.clear()
        original_data.extend(data_var.get())
        editing.set(True)
        refresh_list()
        for row in rows:
            if not row["is_new"]:
                for entry in row["entries"]:
                    entry.configure(state="normal")
                row["delete"].grid()
        edit_btn.grid_forget()
        save_btn.grid(row=999, column=0, padx=10, pady=10, sticky="ew")
        cancel_btn.grid(row=999, column=1, padx=10, pady=10, sticky="ew")

    def save_changes():
        values = []
        for row in rows:
            row_values = [entry.get().strip() for entry in row["entries"]]
            if any(row_values):
                values.append(row_values)
        data_var.set(values)
        if on_save is not None:
            on_save(values)
        editing.set(False)
        refresh_list()
        save_btn.grid_forget()
        cancel_btn.grid_forget()
        edit_btn.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    def cancel_changes():
        data_var.set(original_data.copy())
        editing.set(False)
        refresh_list()
        save_btn.grid_forget()
        cancel_btn.grid_forget()
        edit_btn.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    edit_btn = ctk.CTkButton(
        buttons_frame,
        text="Edit",
        command=enable_edit,
        fg_color="#28a745",
        hover_color="#218838",
        text_color="#ffffff",
        font=font,
        corner_radius=6,
    )
    save_btn = ctk.CTkButton(
        buttons_frame,
        text="Save",
        command=save_changes,
        fg_color="#007bff",
        hover_color="#0069d9",
        text_color="#ffffff",
        font=font,
        corner_radius=6,
    )
    cancel_btn = ctk.CTkButton(
        buttons_frame,
        text="Cancel",
        command=cancel_changes,
        fg_color="#6c757d",
        hover_color="#5a6268",
        text_color="#ffffff",
        font=font,
        corner_radius=6,
    )

    refresh_list()

    buttons_frame.grid(row=999, column=0, columnspan=column_per_rows + 1, sticky="ew")
    edit_btn.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    return container
