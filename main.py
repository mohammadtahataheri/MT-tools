print("start")
import customtkinter

import jdatetime

customtkinter.set_appearance_mode("dark")

app = customtkinter.CTk()
app.geometry("950x700")
app.resizable(True, True)
app.title("MT Tools | برنامه‌ی کاربردی")
app.attributes('-alpha', 0.98)
app.configure(fg_color="#130184")

header_frame = customtkinter.CTkFrame(app)
header_frame.grid(row=0, column=0, sticky="ew")
header_frame.configure(fg_color="#12046C")

header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1) 

title = customtkinter.CTkLabel(
    header_frame, text="MT tools برنامه ی کاربردی", font=("vazirmatn", 26), text_color="#FFFFFF"
)
title.grid(row=0, column=1, sticky="e", padx=30, pady=30)


label = customtkinter.CTkLabel(header_frame, text="", font=("Arial", 26), text_color="#FFFFFF")
label.grid(row=0, column=0, sticky="w", pady=30, padx=30)

def clock():
    now = jdatetime.datetime.now()
    timestr = now.strftime("%H:%M:%S %p  %Y/%m/%d")
    label.configure(text=timestr)
    label.after(1000, clock)

clock()

tab_view = customtkinter.CTkTabview(master=app)
tab_view.grid(row=1, column=0, pady=5, padx=5, sticky="nsew")
tab_view.configure(fg_color="#12046C")

home_tab = tab_view.add("Home")
home_tab.configure(fg_color="#12046C")

home_frame = customtkinter.CTkFrame(master=home_tab)  # ارتفاع پایه بیشتر
home_frame.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
home_frame.configure(fg_color="#12046C")

home_frame.grid_rowconfigure(0, weight=1) # link_frame کش بیاد
home_frame.grid_rowconfigure(1, weight=0) # bottom_frame ثابت باشه
home_frame.grid_columnconfigure(0, weight=1)


home_tab.grid_rowconfigure(0, weight=1)
home_tab.grid_columnconfigure(0, weight=1)

link_frame = customtkinter.CTkFrame(home_frame)
link_frame.grid(row=0, column=0, sticky="nsew", padx=0, pady=(0,10))

link_frame.configure(fg_color="#12046C")


for col in range(3):
    link_frame.grid_columnconfigure(col, weight=1)
for row in range(3):
    link_frame.grid_rowconfigure(row, weight=1)


expend_fram = customtkinter.CTkFrame(home_frame)
expend_fram.grid(row=1, column=0, sticky="nsew", padx=6, pady=(5, 10))
expend_fram.configure(fg_color="#12046C")
expend_fram.grid_columnconfigure(0, weight=1)
expend_fram.grid_columnconfigure(1, weight=1)
expend_fram.grid_rowconfigure(0, weight=1)

def close_tab(tab_name):
    tab_view.delete(tab_name)

def calc_tab():
    from tools import calculator
    tab_name = "calculator"
    n_tab = tab_view.add(tab_name)
    calculator.calc_tab(n_tab)
    close_btn = customtkinter.CTkButton(
        master=n_tab,
        text="❌",
        fg_color="red",
        hover_color="darkred",
        command=lambda name=tab_name: close_tab(name),
        height=5,
        width=5
    )
    close_btn.pack(anchor="ne")

def mtai_tab():
    from tools import mtai
    tab_name = "Hooshang bot"
    n_tab = tab_view.add(tab_name)
    mtai.new_tab(n_tab)
    close_btn = customtkinter.CTkButton(
        master=n_tab,
        text="❌",
        fg_color="red",
        hover_color="darkred",
        command=lambda name=tab_name: close_tab(name),
        height=5,
        width=5
    )
    close_btn.grid(sticky="ne")

def regex_tab():
    from tools import regex
    tab_name = "REGEX"
    n_tab = tab_view.add(tab_name)
    regex.new_tab(n_tab)
    close_btn = customtkinter.CTkButton(
        master=n_tab,
        text="❌",
        fg_color="red",
        hover_color="darkred",
        command=lambda name=tab_name: close_tab(name),
        height=5,
        width=5
    )
    close_btn.grid( sticky="ne")


def searchfile_tab():
    from tools import searchfile
    tab_name = "searchfile"
    n_tab = tab_view.add(tab_name)
    searchfile.new_tab(n_tab)
    close_btn = customtkinter.CTkButton(
        master=n_tab,
        text="❌",
        fg_color="red",
        hover_color="darkred",
        command=lambda name=tab_name: close_tab(name),
        height=5,
        width=5
    )
    close_btn.pack(anchor="ne")


def translate_tab():
    from tools import translate
    tab_name = "Translate"
    n_tab = tab_view.add(tab_name)
    translate.new_tab(n_tab)
    close_btn = customtkinter.CTkButton(
        master=n_tab,
        text="❌",
        fg_color="red",
        hover_color="darkred",
        command=lambda name=tab_name: close_tab(name),
        height=5,
        width=5
    )
    close_btn.grid(sticky="ne")

def open_camscan():
    from tools import camscan
    camscan.new_win()

def sysmonitor_tab():
    from tools import sys_monitor
    tab_name = "system monitor"
    n_tab = tab_view.add(tab_name)
    sys_monitor.new_tab(n_tab)
    close_btn = customtkinter.CTkButton(
        master=n_tab,
        text="❌",
        fg_color="red",
        hover_color="darkred",
        command=lambda name=tab_name: close_tab(name),
        height=5,
        width=5
    )
    close_btn.pack(anchor="ne")

def iptest_tab():
    from tools import iptest
    tab_name = "test ip"
    n_tab = tab_view.add(tab_name)
    iptest.new_tab(n_tab)
    close_btn = customtkinter.CTkButton(
        master=n_tab,
        text="❌",
        fg_color="red",
        hover_color="darkred",
        command=lambda name=tab_name: close_tab(name),
        height=5,
        width=5
    )
    close_btn.pack(anchor="ne")


def json_creat_tab():
    from tools import json_creat
    tab_name = "JSON"
    n_tab = tab_view.add(tab_name)
    json_creat.new_tab(n_tab)
    close_btn = customtkinter.CTkButton(
        master=n_tab,
        text="❌",
        fg_color="red",
        hover_color="darkred",
        command=lambda name=tab_name: close_tab(name),
        height=5,
        width=5
    )
    close_btn.pack(anchor="ne")

def open_mini_terminal():
    from tools import aa
    tab_name = "Terminal"
    n_tab = tab_view.add(tab_name)
    print("tab opened")
    aa.new_tab(n_tab, app, lambda: close_tab(tab_name))
    print("tab close")

def open_pyrun_tab():
    from tools import py_run
    tab_name = "Python IDE"
    n_tab = tab_view.add(tab_name)
    close_btn = customtkinter.CTkButton(
        master=n_tab,
        text="❌",
        fg_color="red",
        hover_color="darkred",
        command=lambda name=tab_name: close_tab(name),
        height=5,
        width=5
    )
    close_btn.pack(anchor="ne", padx=10, pady=10)
    py_run.setup_python_runner_widget(n_tab)



buttons_link = [
    ("ماشین حساب", calc_tab),
    ("چت بات", mtai_tab),
    ("جستوجو فایل", searchfile_tab),
    ("جدا سازی حروف", regex_tab),
    ("ترجمه گر", translate_tab),
    ("اسکن کامرا", open_camscan),
    ("دما و استفاده", sysmonitor_tab),
    ("ادرس شبکه", iptest_tab),
    ("جدول اطلاعات", json_creat_tab)
]

for i, (text, cmd) in enumerate(buttons_link):
    row = i // 3
    col = i % 3
    btn = customtkinter.CTkButton(link_frame, text=text, command=cmd, font=("vazirmatn", 35))
    btn.grid(row=row, column=col, padx=7, pady=7, sticky="nsew")
    btn.configure(fg_color="#3A2DEB", hover_color="#402FAF")


btn_expand = customtkinter.CTkButton(expend_fram, text="ترمینال حرفه ای", command=open_mini_terminal, font=("vazirmatn", 35))
btn_expand.grid(row=0, column=0, padx=(0, 5), pady=(0, 5), sticky="nsew")
btn_expand.configure(fg_color="#3A2DEB", hover_color="#402FAF")

btn_expand2 = customtkinter.CTkButton(expend_fram, text="ادیتور پایتون", command=open_pyrun_tab, font=("vazirmatn", 35))
btn_expand2.grid(row=0, column=1, padx=(5, 0), pady=(0, 5), sticky="nsew")
btn_expand2.configure(fg_color="#3A2DEB", hover_color="#402FAF")

bottom_frame = customtkinter.CTkFrame(home_frame)
bottom_frame.grid(row=2, column=0, sticky="ew", padx=0, pady=(10,0))
bottom_frame.configure(fg_color="#12046C")
bottom_frame.grid_columnconfigure(0, weight=1)
bottom_frame.grid_columnconfigure(1, weight=1)

def about():
    win = customtkinter.CTk()
    win.geometry("700x510")
    win.title("سوالات متداول")
    win.resizable(False, False)
    lable = customtkinter.CTkLabel(
        win,
        text="""
اگر فونت برنامه نصب نشد فایل vazirmatn.ttf را اجرا نمایید

به خاطر ملی بودن اینترنت امکان اختلال در ساختار برنامه وجود دارد

برای بستن ترمینال حرفه ای از دستورات استفاده کنید

version : 2.0
©1404 تمامی حقوق محفوظ است
""",
        font=("vazirmatn", 20)
    )
    lable.pack(fill="both", expand=True)
    win.mainloop()

about_btn = customtkinter.CTkButton(bottom_frame, text="سوالات متداول", font=("vazirmatn", 30), command=about)
about_btn.grid(row=0, column=0, padx=10, pady=5, sticky="w")
about_btn.configure(fg_color="#3A2DEB", hover_color="#402FAF")

lable_ab = customtkinter.CTkLabel(
    bottom_frame,
    text="""
    تمامی حقوق برنامه متعلق به
    محمد طاها طاهری است. 1404-1405
""",
    font=("vazirmatn", 27),
    anchor="w", 
    text_color="#FFFFFF"
)
lable_ab.grid(row=0, column=1, padx=10, pady=5, sticky="e")

# app.grid_rowconfigure(0, weight=0)  # header ثابت
# app.grid_rowconfigure(1, weight=1)  # tab کش بیاد
# # app.grid_rowconfigure(2, weight=0)  # bottom ثابت
app.grid_columnconfigure(0, weight=1)



app.mainloop()