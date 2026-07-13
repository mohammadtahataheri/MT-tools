import customtkinter , os, threading, string

def new_tab(parent_frame):




    entry = customtkinter.CTkEntry(master=parent_frame,placeholder_text="نام فایل", font=("vazirmatn", 20), height=50)
    entry.pack(padx=10,pady=10,fill="x")

    text = customtkinter.CTkTextbox(master=parent_frame, font=("vazirmatn", 24), height=400)
    text.pack(padx=10,pady=10,fill="both",expand=True)

    def get_all_drivers():
        drivers = []
        for letter in string.ascii_uppercase:
            drive = f"{letter}:\\"
            if os.path.exists(drive):
                drivers.append(drive)
        return drivers

    def search_file_global():
        keyword = entry.get().strip()
        text.delete("1.0", "end")
        if keyword == "":
            text.insert("1.0", "لطفا نام فایل را وارد کنید")
            return
        drivers = get_all_drivers()
        found = 0
        for driver in drivers:
            text.insert("end", f"درایور {driver}\n")
            
            for root, dirs, files in os.walk(driver):
                for file in files:
                    if keyword.lower() in file.lower():
                        text.insert("end", f"name: {file} In: {root}\n")
                        found += 1

        if found == 0:
            text.insert("end", "فایلی یافت نشد")
        

    def start_search():
        
        threading.Thread(target=search_file_global, daemon=True).start()

    btn = customtkinter.CTkButton(master=parent_frame,text="جستجو",command=start_search,font=("vazirmatn", 24))
    btn.pack(padx=10,pady=10)


