import customtkinter as ctk
from tkinter import *
from tkinter import ttk

def create_treeview(
        root, 
        columns=["Column_1", "Column_2"], 
        col_width=300,
        height=15,
        data=[
            ("row 1 column 1 data", "row 1 column 2 data"),
            ("row 2 column 1 data", "row 2 column 2 data")
        ],
        col_bg="#2D2F33",
        content_bg="#1E1F23",
        text_color="#E4E6EB",
        heading_text_color="#F5F6FA",
        data_bg="#2A2C30",
        data_bg_2="#242629",
        alternating_data_bg=True,
        row_height=50,
        font=("Segoe UI", 14),
        
        # For the live search feature
        searchable=True,
        search_label="Search for: ",
        search_box_bg_color="white",
        search_box_text_color="black"
    ):

    style = ttk.Style()
    style.theme_use("default")

    style.configure(
        "Custom.Treeview",
        background=content_bg,
        fieldbackground=content_bg,
        foreground=text_color,
        rowheight=row_height,
        font=font
    )
    style.configure(
        "Custom.Treeview.Heading",
        background=col_bg,
        foreground=heading_text_color,
        font=(font[0], font[1], "bold")
    )

    content = ctk.CTkFrame(root, corner_radius=0, fg_color=content_bg)

    # Search area
    if searchable:
        search_frame = ctk.CTkFrame(content, fg_color=content_bg)

        search_label_widget = ctk.CTkLabel(search_frame, text=search_label, text_color=text_color, font=font)
        search_label_widget.pack(side=LEFT, padx=(5, 0))

        search_var = StringVar()
        search_entry = ctk.CTkEntry(search_frame, textvariable=search_var, font=font)
        search_entry.configure(fg_color=search_box_bg_color, text_color=search_box_text_color)
        search_entry.pack(side=LEFT, padx=5)

        in_label = ctk.CTkLabel(search_frame, text="in", text_color=text_color, font=font)
        in_label.pack(side=LEFT, padx=(0,5))

        combo = ctk.CTkComboBox(search_frame, values=columns, font=font, state="readonly")
        combo.set(columns[0])
        combo.pack(side=LEFT, padx=5)

        search_frame.pack(fill=X, pady=(15, 15), padx=5)

        # Bind to update width dynamically:
        def update_entry_width(event):
            window_width = event.width
            char_width = max(10, int((window_width * 0.5) / 2))
            search_entry.configure(width=char_width)

        content.bind("<Configure>", update_entry_width)


    # Treeview
    tree = ttk.Treeview(content, columns=columns, height=height, style="Custom.Treeview")
    tree.column("#0", width=0, stretch=False)
    tree.heading("#0", text="")

    tree.tag_configure("bg1", background=data_bg)
    tree.tag_configure("bg2", background=data_bg_2)

    for item in columns:
        tree.column(item, anchor=W, width=col_width)
        tree.heading(item, text=item, anchor=W)

    # Store all data to support filtering
    all_data = list(data)

    def populate_tree(filtered_data):
        tree.delete(*tree.get_children())
        for index, row in enumerate(filtered_data):
            tag = "bg1" if not alternating_data_bg or index % 2 == 0 else "bg2"
            tree.insert("", END, values=row, tags=(tag,))

    populate_tree(all_data)

    if searchable:
        def on_search(*args):
            query = search_var.get().lower()
            col_index = columns.index(combo.get())
            filtered = [row for row in all_data if query in str(row[col_index]).lower()]
            populate_tree(filtered)

        search_var.trace_add("write", on_search)

    vsb = Scrollbar(content, orient=VERTICAL, command=tree.yview)
    hsb = Scrollbar(content, orient=HORIZONTAL, command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    vsb.pack(side=RIGHT, fill=Y)
    hsb.pack(side=BOTTOM, fill=X)
    tree.pack(expand=True, fill=BOTH)

    return content