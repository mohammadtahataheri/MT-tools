import customtkinter
import io
import sys
from contextlib import redirect_stdout

# --- تابع اجرای کد (مخصوص ویجت‌های داخل تب) ---
# این تابع نیاز به دسترسی به inp و out دارد که توسط setup_python_runner_widget ساخته شده‌اند.
# ما آنها را به عنوان آرگومان دریافت می‌کنیم.
def run_code_in_widget(input_textbox, output_textbox):
    try:
        code = input_textbox.get("1.0", "end-1c")

        stdout_capture = io.StringIO()
        # فضای نام (globals) را برای exec خالی می‌گذاریم تا از تداخل جلوگیری شود.
        exec_globals = {}
        with redirect_stdout(stdout_capture):
            exec(code, exec_globals, {})
            pass
        stdout_value = stdout_capture.getvalue()

        output_textbox.configure(state="normal")
        output_textbox.delete("1.0", "end")
        output_textbox.insert("1.0", stdout_value)
        output_textbox.configure(state="disabled")

    except Exception as e:
        output_textbox.configure(state="normal")
        output_textbox.delete("1.0", "end")
        output_textbox.insert("1.0", str(e)) # تبدیل استثنا به رشته
        output_textbox.configure(state="disabled")

# --- تابع برای تنظیم ویجت‌های Python Runner در یک فریم والد ---
def setup_python_runner_widget(parent_frame):
    """
    این تابع ویجت‌های مربوط به اجرای کد پایتون را در parent_frame ایجاد و پیکربندی می‌کند.
    این تابع جایگزین کد اصلی py-run.py شده و ویجت‌ها را به parent_frame اضافه می‌کند.
    """
    inp = customtkinter.CTkTextbox(master=parent_frame, font=("vazirmatn", 16))
    inp.pack(expand=True, fill="both", pady=10, padx=10)

    # اتصال دکمه به تابع run_code_in_widget با پاس دادن ویجت‌های inp و out
    btn = customtkinter.CTkButton(master=parent_frame, text="Run Code", command=lambda: run_code_in_widget(inp, out))
    btn.pack(pady=10)

    out = customtkinter.CTkTextbox(master=parent_frame, font=("vazirmatn", 16))
    out.pack(expand=True, fill="both", pady=10, padx=10)
    out.configure(state="disabled")

    # این تابع ویجت‌های ساخته شده را برمی‌گرداند تا بتوانیم در صورت نیاز به آنها دسترسی داشته باشیم
    return inp, btn, out

# --- تابع برای تنظیم ویجت‌های برنامک جدید در یک فریم والد ---
def setup_my_new_widget(parent_frame):
    """
    این تابع ویجت‌های برنامک جدید (مثلاً یک label و یک entry) را در parent_frame ایجاد می‌کند.
    """
    new_label = customtkinter.CTkLabel(master=parent_frame, text="این یک برنامک جدید است!", font=("vazirmatn", 20))
    new_label.pack(pady=20, padx=20)

    new_entry = customtkinter.CTkEntry(master=parent_frame, placeholder_text="یک ورودی اینجا...", font=("vazirmatn", 18))
    new_entry.pack(pady=10, padx=20, fill="x")



