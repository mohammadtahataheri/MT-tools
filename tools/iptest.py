import customtkinter
import requests
import socket
import threading
def new_tab(parent_frame):

    def show_ip():
        try:
            # IP عمومی
            public_ip = requests.get("https://api.ipify.org", timeout=1).text
        except:
            public_ip = "Turn off your dns or change your wifi"

        # IP محلی
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)

        text.configure(state="normal")
        text.delete("1.0", "end")
        text.insert("1.0", f"🌐 Public IP: {public_ip}\n💻 Local IP: {local_ip}")
        text.configure(state="disabled")

    # ساخت پنجره
    threading.Thread(target=show_ip, daemon=True).start()


    text = customtkinter.CTkTextbox(master=parent_frame, font=("vazirmatn",35), width=900, height=400)
    text.pack(pady=10, padx=10)
    text.configure(state="disabled")

    refresh_btn = customtkinter.CTkButton(master=parent_frame, text="Refresh IP", command=show_ip)
    refresh_btn.pack(pady=5)

    # نمایش IP اولیه
    show_ip()



