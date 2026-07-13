import psutil
import customtkinter


def new_tab(parent_frame):

    
    CPU_limit = 90
    RAM_limit = 90

    text = customtkinter.CTkTextbox(
        master=parent_frame, font=("vazirmatn", 80), width=750, height=450
    )
    text.pack()
    text.configure(state="disabled")

    def update_stats():
        cpu = psutil.cpu_percent(interval=None)
        ram = psutil.virtual_memory().percent

        text.configure(state="normal")
        text.delete("1.0", "end")

        if cpu > CPU_limit:
            text.insert("1.0", f"⚠ CPU HIGH\n{cpu}%")
        elif ram > RAM_limit:
            text.insert("1.0", f"⚠ RAM HIGH\n{ram}%")
        else:
            text.insert("1.0", f"CPU: {cpu}%\nRAM: {ram}%")

        text.configure(state="disabled")

        parent_frame.after(500, update_stats)  

    update_stats()




