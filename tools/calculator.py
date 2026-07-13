import customtkinter as ctk
import numexpr as ne
def calc_tab(parent_frame):
    # ================= app =================
    # main = ctk.CTk()
    # main.geometry("500x600")
    # main.title("Calculator")
    # main.configure(fg_color="#0F0359")
    # main.resizable(False, False)
    # main.attributes('-alpha',0.98)

    # ================= main frame =================
    main_frame = ctk.CTkFrame(master=parent_frame)
    main_frame.pack(expand=True, fill="both", padx=10, pady=10)
    main_frame.configure(fg_color="#12046C")

    # ================= entry =================
    entry = ctk.CTkEntry(
        main_frame,
        placeholder_text="0",
        font=("Arial", 60),
        width=600,
        height=120
    )
    entry.pack(fill="x", pady=(0, 15))

    # ================= button frame =================
    button_frame = ctk.CTkFrame(main_frame)
    button_frame.pack(expand=True, fill="both")
    button_frame.configure(fg_color="#4A3BA8")


    for i in range(4):
        button_frame.grid_columnconfigure(i, weight=1)
    for i in range(5):
        button_frame.grid_rowconfigure(i, weight=1)

    # ================= functions =================
    def add(value):
        entry.insert("end", value)

    # ================= buttons =================
    buttons = [
        ("C", 0, 0,"#7E00F3"),("%", 0, 1,"#7E00F3"),("⌫", 0, 2,"#7E00F3"),("÷", 0, 3,"#0B89FF"),
        ("7", 1, 0,"#12046C"),("8", 1, 1,"#12046C"),("9", 1, 2,"#12046C"),("×", 1, 3,"#0B89FF"),
        ("4", 2, 0,"#12046C"),("5", 2, 1,"#12046C"),("6", 2, 2,"#12046C"),("-", 2, 3,"#0B89FF"),
        ("1", 3, 0,"#12046C"),("2", 3, 1,"#12046C"),("3", 3, 2,"#12046C"),("+", 3, 3,"#0B89FF"),
        ("0", 4, 0,"#12046C"),("00", 4, 1,"#12046C"),(".", 4, 2,"#12046C"),("=", 4, 3,"#7E00F3")
    ]
    def calculate():
        try:
            
            expression = entry.get().replace("×", "*").replace("÷", "/")
            result = ne.evaluate(expression)
            entry.delete(0, "end")      
            entry.insert(0, str(result)) 
        except:
            entry.delete(0, "end")
            entry.insert(0, "Error")

    def backspace():
        current = entry.get()
        entry.delete(0, "end")
        entry.insert(0, current[:-1])

    height = 70
    for text, row, col, color in buttons:
        if text == "=":
            btn = ctk.CTkButton(
                button_frame,
                text=text,
                command=calculate,   
                font=("Arial", 30),
                height= height
            )
        elif text == "C":
            btn = ctk.CTkButton(
                button_frame,
                text=text,
                command=lambda: entry.delete(0, "end"), 
                font=("Arial", 30),
                height=height
            )
        elif text == "⌫":
            btn = ctk.CTkButton(
                button_frame,
                text=text,
                command=backspace,
                font=("Arial", 30),
                height= height
            )

        else:
            btn = ctk.CTkButton(
                button_frame,
                text=text,
                command=lambda t=text: add(t),
                font=("Arial", 30),
                height= height
            )

        btn.grid(row=row, column=col, padx=7, pady=7, sticky="nsew")
        btn.configure(fg_color=color, hover_color="#402FAF")



