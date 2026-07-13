import re
import customtkinter

def new_tab(parent_frame):

    parent_frame.grid_rowconfigure(0, weight=1)
    parent_frame.grid_rowconfigure(1, weight=1)
    parent_frame.grid_columnconfigure(0, weight=1)


    textbox = customtkinter.CTkTextbox(master=parent_frame,font=("vazirmatn",26),width=750, height=470)
    textbox.grid(row=0,column=0)

    def show_win(matches):
        win = customtkinter.CTk()
        win.geometry("600x450")
        win.resizable(False, False)
        win.configure(fg_color="#130184")
        win.title(" ")
        win.attributes('-alpha',0.98)

        textb = customtkinter.CTkTextbox(win,width=600,height=450,font=("vazirmatn",26))
        textb.pack()
        textb.insert("1.0",matches)
        win.mainloop()
    
    # تابع برای پیدا کردن اعداد انگلیسی

    mapping = {
            "a": "q", "b": "w", "c": "r", "d": "o", "e": "z",
            "f": "s", "g": "y", "h": "i", "i": "e", "j": "p",
            "k": "a", "l": "u", "m": "d", "n": "f", "o": "g",
            "p": "h", "q": "j", "r": "k", "s": "l", "t": "t",
            "u": "x", "v": "c", "w": "v", "x": "b", "y": "n",
            "z": "m",
            "A": "Q", "B": "W", "C": "R", "D": "O", "E": "Z",
            "F": "S", "G": "Y", "H": "I", "I": "E", "J": "P",
            "K": "A", "L": "U", "M": "D", "N": "F", "O": "G",
            "P": "H", "Q": "J", "R": "K", "S": "L", "T": "T",
            "U": "X", "V": "C", "W": "V", "X": "B", "Y": "N",
            "Z": "M"
    }

        # ساخت دیکشنری برعکس برای decrypt
    reverse_mapping = {v: k for k, v in mapping.items()}

    def encrypt():
        text = textbox.get("1.0", "end")
        res = ""
        result = ""
        for char in text:
            if char in mapping:
                res += mapping[char]
            else:
                res += char

        for char in res:
            if char in mapping:
                result += mapping[char]
            else:
                result += char
        show_win(result)

    def decrypt():
        text = textbox.get("1.0", "end")
        res = ""
        result = ""
        for char in text:
            if char in reverse_mapping:
                res += reverse_mapping[char]
            else:
                res += char

        for char in res:
            if char in mapping:
                result += reverse_mapping[char]
            else:
                result += char
        show_win(result)

    button_frame = customtkinter.CTkFrame(master=parent_frame)
    button_frame.configure(fg_color="#130184")
    button_frame.grid(row=0,column=1)
    button1 = customtkinter.CTkButton(button_frame,text="رمز گزاری",command=encrypt,font=("vazirmatn",30), width=200)
    button1.grid(row=0,column=0,pady=5)
    button2 = customtkinter.CTkButton(button_frame,text="رمز گشایی",command=decrypt,font=("vazirmatn",30), width=200)
    button2.grid(row=1,column=0,pady=5)

