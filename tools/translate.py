import customtkinter
from deep_translator import GoogleTranslator



def new_tab(parent_frame):
    
    parent_frame.grid_rowconfigure(0, weight=1)
    parent_frame.grid_rowconfigure(1, weight=1)
    parent_frame.grid_rowconfigure(2, weight=1)
    parent_frame.grid_rowconfigure(3, weight=1)
    parent_frame.grid_columnconfigure(0, weight=1)

    enter = customtkinter.CTkTextbox(master=parent_frame,font=("vazirmatn", 22))
    enter.grid(row=0,column=0,sticky="ew",padx=10,pady=10)

    out = customtkinter.CTkTextbox(master=parent_frame,font=("vazirmatn", 22))
    out.configure(state="disabled")
    out.grid(row=1,column=0,sticky="ew",padx=10,pady=10)

    btn1 = customtkinter.CTkButton(master=parent_frame,text="انگلیسی به فارسی",font=("vazirmatn", 22),command=lambda: trans("انگلیسی به فارسی"))
    btn1.grid(row=2,column=0,sticky="ew",padx=10,pady=10)

    btn2 = customtkinter.CTkButton(master=parent_frame,text="فارسی به انگلیسی",font=("vazirmatn", 22),command=lambda: trans("فارسی به انگلیسی"))
    btn2.grid(row=3,column=0,sticky="ew",padx=10,pady=10)

    def trans(transtype):
        
        text = enter.get("1.0", "end")
        if not text:
            out.insert("1.0", "متنی وارد نشده")
            return

        try:
            if transtype == "انگلیسی به فارسی":
                out.configure(state="normal")
                out.delete("1.0", "end")
                out.insert("1.0", GoogleTranslator(source="en", target="fa").translate(text))
                out.configure(state="disabled")
            elif transtype == "فارسی به انگلیسی":
                out.configure(state="normal")                
                out.delete("1.0", "end")
                out.insert("1.0", GoogleTranslator(source="fa", target="en").translate(text))
                out.configure(state="normal")                
        except:
            out.insert("1.0", "خطا در ترجمه ❌")


