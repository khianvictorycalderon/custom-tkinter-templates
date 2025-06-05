import customtkinter as ctk
from tkinter import *
from tkinter import ttk

def create_treeview(
        root, 
        
        # Data & Columns
        columns=["Column_1", "Column_2"], 
        data=[
            ("row 1 column 1 data", "row 1 column 2 data"),
            ("row 2 column 1 data", "row 2 column 2 data")
        ],
        
        # Sizes
        column_width=300,
        height=15,
        
        # General (Applies to all)
        content_bg="#1E1F23",
        text_color="#E4E6EB",
        font=("Segoe UI", 13),
        
        # Rows
        alternate_row_bg=True,
        row_a_bg="#2A2C30",
        row_b_bg="#242629",
        row_height=50,
        
        # Header
        header_bg_color="#1E1F23",
        header_text_color="#F5F6FA",
        
        # For the live search feature
        searchable=True,
        search_label="Search for: ",
        search_box_bg_color="white",
        search_box_text_color="black",
        
        # Dropdown
        dropdown_bg_color="white",
        dropdown_text_color="black"
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
        background=header_bg_color,
        foreground=header_text_color,
        font=(font[0], font[1], "bold")
    )

    content = ctk.CTkFrame(root, corner_radius=0, fg_color=content_bg)
    
    all_data = list(data)

    # Treeview setup
    tree = ttk.Treeview(content, columns=columns, height=height, style="Custom.Treeview")
    tree.column("#0", width=0, stretch=False)
    tree.heading("#0", text="")

    tree.tag_configure("bg1", background=row_a_bg)
    tree.tag_configure("bg2", background=row_b_bg)

    for item in columns:
        tree.column(item, anchor=W, width=column_width)
        tree.heading(item, text=item, anchor=W)

    def populate_tree(filtered_data):
        tree.delete(*tree.get_children())
        for index, row in enumerate(filtered_data):
            tag = "bg1" if not alternate_row_bg or index % 2 == 0 else "bg2"
            tree.insert("", END, values=row, tags=(tag,))

    populate_tree(all_data)

    if searchable:
        search_frame = ctk.CTkFrame(content, fg_color=content_bg)

        # Variables
        search_var = StringVar()
        case_sensitive = BooleanVar()
        exact_match = BooleanVar()

        # Left controls frame for search label, entry, dropdown, checkboxes
        search_controls = ctk.CTkFrame(search_frame, fg_color=content_bg)
        
        search_label_widget = ctk.CTkLabel(search_controls, text=search_label, text_color=text_color, font=font)
        search_label_widget.pack(side=LEFT, padx=(5, 0))

        search_entry = ctk.CTkEntry(search_controls, textvariable=search_var, font=font)
        search_entry.configure(fg_color=search_box_bg_color, text_color=search_box_text_color)
        search_entry.pack(side=LEFT, padx=5)

        in_label = ctk.CTkLabel(search_controls, text="in", text_color=text_color, font=font)
        in_label.pack(side=LEFT, padx=(0, 5))

        combo_var = StringVar(value=columns[0])
        combo = ctk.CTkOptionMenu(search_controls, values=columns, font=font, state="readonly",
                                variable=combo_var,
                                fg_color=dropdown_bg_color, text_color=dropdown_text_color,
                                button_color=dropdown_bg_color, button_hover_color=dropdown_bg_color)
        combo.pack(side=LEFT, padx=5)

        # Define on_search here so it can access populate_tree
        def on_search(*args):
            query = search_var.get()
            col_index = columns.index(combo.get())
            is_case_sensitive = case_sensitive.get()
            is_exact = exact_match.get()

            if not is_case_sensitive:
                query = query.lower()

            if query:
                def match(value):
                    val = value if is_case_sensitive else str(value).lower()
                    return val == query if is_exact else query in val

                filtered = [row for row in all_data if match(row[col_index])]
                populate_tree(filtered)
                results_label.configure(text=f"{len(filtered)} result{'s' if len(filtered) != 1 else ''}")
            else:
                populate_tree(all_data)
                results_label.configure(text=f"{len(all_data)} row{'s' if len(all_data) != 1 else ''}")

        case_checkbox = ctk.CTkCheckBox(search_controls, text="Case-Sensitive", variable=case_sensitive, 
                                        text_color=text_color, font=font, command=on_search)
        case_checkbox.pack(side=LEFT, padx=(10, 0))

        whole_word_checkbox = ctk.CTkCheckBox(search_controls, text="Whole Word Only", variable=exact_match, 
                                         text_color=text_color, font=font, command=on_search)
        whole_word_checkbox.pack(side=LEFT, padx=(10, 0))

        search_controls.pack(side=LEFT, padx=(5, 0))
        
        # Bind combo variable change to refresh search
        combo_var.trace_add("write", on_search)

        results_label = ctk.CTkLabel(search_frame, text=f"{len(all_data)} rows", text_color=text_color, font=font)
        results_label.pack(side=RIGHT, padx=(0, 10))

        search_frame.pack(fill=X, pady=(15, 15), padx=5)

        search_var.trace_add("write", on_search)
        on_search()

        def update_entry_width(event):
            window_width = event.width
            char_width = max(10, int((window_width * 0.5) / 2))
            search_entry.configure(width=char_width)

        content.bind("<Configure>", update_entry_width)

    vsb = Scrollbar(content, orient=VERTICAL, command=tree.yview)
    hsb = Scrollbar(content, orient=HORIZONTAL, command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    vsb.pack(side=RIGHT, fill=Y)
    hsb.pack(side=BOTTOM, fill=X)
    tree.pack(expand=True, fill=BOTH)

    return content
