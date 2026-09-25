# استفاده از سرویس گپ جی‌پی‌تی با Python
import openai
from openai import OpenAI
import customtkinter
import threading


# ایجاد یک نمونه از کلاینت با کلید API
client = OpenAI(
    api_key='api',
    base_url='https://api.gapgpt.app/v1'
)
SYSTEM_PROMPT = """
تو یک چت‌بات فارسی هستی.
نام تو «هوشنگ» است.
اگر کاربر به هر شکلی درباره نام تو سؤال کرد
(مستقیم، غیرمستقیم، شوخی، کنایه، یا با جمله‌های متفاوت)،
باید بفهمی منظورش نام توست و پاسخ بده که نامت هوشنگ است.
و اگر کاربر سلام کرد اسمت رو بهش بگو برای مثال:من هوشنگ در خدمت شما هستم
و بیشتر از یکبار هم سلام نکن
توسعه دهنده ی تو تیم برنامه نویسی MT tools هست
"""
chat_memory = []

def send_message(message):
    global chat_memory

    chat_memory.append({"role": "user", "content": message})

    messages_to_send = [{"role": "system", "content": SYSTEM_PROMPT}] + chat_memory

    try:

        response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages_to_send 
        )

        assistant_reply = response.choices[0].message.content

        chat_memory.append({"role": "assistant", "content": assistant_reply})

        return assistant_reply
    
    except Exception as e:
        # مدیریت خطا در صورت بروز مشکل در ارتباط با API یا پردازش
        print(f"An error occurred: {e}")
        return "متاسفم، مشکلی در پردازش پیام رخ داد."


 
def new_tab(parent_frame):

    parent_frame.grid_rowconfigure(1, weight=1) 
    parent_frame.grid_columnconfigure(0, weight=1)


    text = customtkinter.CTkTextbox(master=parent_frame, font=("vazirmatn", 24), height=500)
    text.configure("justify_text", wrap="word")
    text.grid(row=0, column=0, sticky="nsew", columnspan=2)

    

    input = customtkinter.CTkEntry(master=parent_frame, font=("vazirmatn", 24))
    input.grid(row=1, column=0, sticky="nsew",padx=10, pady=10)




    text = customtkinter.CTkTextbox(
    master=parent_frame, font=("vazirmatn", 24), width=800, height=450
    )
    text.grid(row=0, column=0, sticky="nsew", columnspan=2)

    text.tag_config("right", justify="right")

    spinner_frames = ["/", "-", "\\", "|"]
    spinner_index = 0
    loading = False

    spinner_label = customtkinter.CTkLabel(master=parent_frame,text="",font=("vazirmatn",14),text_color="#FFFFFF")
    spinner_label.grid(row=2, column=0, columnspan=2)

    def animate_spinner():
        nonlocal spinner_index, loading
        if loading:
            frame = spinner_frames[spinner_index % len(spinner_frames)]
            spinner_label.configure(text=f"{frame} درحال پردازش")
            spinner_index += 1
            parent_frame.after(150, animate_spinner)
        else:
            spinner_label.configure(text="")

    def ask_gpt(message):
        nonlocal loading

        response = send_message(message)


        text.insert("end", f"هوشنگ: {response}\n\n", "justify_text")
        text.see("end") # این خط باعث میشه اسکرول همیشه پایین بمونه


        loading = False

    def send():
        nonlocal loading
        message = input.get()
        if not message:
            return
        text.insert("end", f"شما: {message}\n\n", "right")
        input.delete(0, "end")

        loading = True
        animate_spinner()

        threading.Thread(target=ask_gpt, args=(message,), daemon=True).start()        

    input.bind("<Return>", lambda event: send())

    button = customtkinter.CTkButton(master=parent_frame, text="ارسال", font=("vazirmatn", 24), command=send, fg_color="#3A2DEB", hover_color="#402FAF")
    button.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

