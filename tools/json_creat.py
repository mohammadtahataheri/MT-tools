import customtkinter
from tkinter import filedialog
import json

def new_tab(parent_frame):
    entries = []

    table_frame = customtkinter.CTkScrollableFrame(
        master=parent_frame,
        label_text="لیست متغیرها",
        label_font=("vazirmatn", 14),
        height=340
    )
    table_frame.pack(pady=20, padx=20, fill="both", expand=True)
    table_frame.configure(fg_color="#100276")

    table_frame.grid_columnconfigure(0, weight=1)
    table_frame.grid_columnconfigure(1, weight=1)

    customtkinter.CTkLabel(table_frame, text="نام متغیر", font=("vazirmatn", 20)).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    customtkinter.CTkLabel(table_frame, text="مقدار متغیر", font=("vazirmatn", 20)).grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    def add_row(row_num):
        name_entry = customtkinter.CTkEntry(
            table_frame,
            placeholder_text="نام متغیر",
            font=("vazirmatn", 22),
            height=60
        )
        name_entry.grid(row=row_num, column=0, pady=5, padx=5, sticky="ew")

        value_entry = customtkinter.CTkEntry(
            table_frame,
            placeholder_text="مقدار متغیر",
            font=("vazirmatn", 22),
            height=60
        )
        value_entry.grid(row=row_num, column=1, pady=5, padx=5, sticky="ew")

        entries.append((name_entry, value_entry))

    add_row(1)
    row_counter = 2

    def add_new_row():
        nonlocal row_counter
        add_row(row_counter)
        row_counter += 1

    add_row_btn = customtkinter.CTkButton(
        master=parent_frame,
        text="افزودن ردیف جدید",
        command=add_new_row,
        font=("vazirmatn", 20)
    )
    add_row_btn.pack(pady=10)

    result_label = customtkinter.CTkLabel(
        master=parent_frame,
        text="",
        font=("vazirmatn", 20)
    )
    result_label.pack(pady=10)

    def save_json():
        data = {}
        for name_entry, value_entry in entries:
            key = name_entry.get().strip()
            value = value_entry.get()
            if key:
                data[key] = value

        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json")],
            title="محل ذخیره JSON را انتخاب کنید"
        )

        if not file_path:
            return

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            result_label.configure(text=f"✅ JSON ساخته شد:\n{file_path}")
        except Exception as e:
            result_label.configure(text=f"❌ خطا در ذخیره فایل:\n{e}")

    save_btn = customtkinter.CTkButton(
        master=parent_frame,
        text="ساخت JSON",
        command=save_json,
        font=("vazirmatn", 20)
    )
    save_btn.pack(pady=10)
