import customtkinter as ctk
import threading
import queue

def new_tab(parentframe, root, close):



    output = ctk.CTkTextbox(master=parentframe,width=1050, height=500, font=("vazirmatn",30))
    output.pack(pady=10)
    output.insert("end", ">>> System Ready...\n")
    output.configure(state="disabled")

    entry = ctk.CTkEntry(master=parentframe, width=1200, font=("vazirmatn",18))
    entry.pack(side="left", padx=10, pady=10)

    spinner_label = ctk.CTkLabel(master=parentframe, text="", font=("vazirmatn",14))
    spinner_label.pack()

    spinner_frames = ["/", "-", "\\", "|"]
    spinner_index = 0
    loading = False

    # صف برای Thread-Safe ارتباط با GUI
    gui_queue = queue.Queue()

    # --------- Command Functions ---------
    def help(args):
        return '''
"help": show this message,
"print": print a text,
"exit": delete terminal tab,
"clear": clear terminal,
"time": show_time,
"whoami": show user propertis,
"sysinfo": system info,
"cmd": run terminal cmd in C:\\Users\\<user>>,
"close": close app,
"uptime": time your pc on,
"matrix":show letter matrix,
"activate1":activate your windows step 1,
"activate2":activate your windows step 2,
"rand_num":random number,
"flip_coin":flip_coin,
"roll_dice":roll_dice'''

    def exit_tab(args=None):
        close()


    def echo(args):
        return " ".join(args)
    
    def clear(args=None):
        output.configure(state="normal")
        output.delete("1.0","end")
        output.configure(state="disabled")

    def show_time(args=None):
        import datetime
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def whoami(args=None):
        import os
        return os.getlogin()
    
    def sysinfo(args=None):
        import os, psutil, platform
        cpu = platform.processor()
        system = platform.system()
        release = platform.release()
        version = platform.version()
        machine = platform.machine()
        ram = round(psutil.virtual_memory().total / (1024**3), 2)
        cores = psutil.cpu_count(logical=True)
        info = f"""
System: {system} {release}
Version: {version}
Machine: {machine}
Processor: {cpu}
CPU Cores: {cores}
RAM: {ram} GB
Current Directory: {os.getcwd()}
"""
        return info.strip()
    
    def run_cmd(args):
        import subprocess, os
        if not args: return "Usage: cmd <command>"
        try:
            result = subprocess.run(args, capture_output=True, text=True, shell=True, cwd=os.path.expanduser("~"))
            output_text = result.stdout if result.stdout else result.stderr
            return output_text.strip() if output_text else "Done."
        except Exception as e:
            return f"Error: {str(e)}"
        
    def exit_main(args=None):
        root.destroy()

    def uptime(args=None):
        import psutil
        import datetime
        return str(datetime.datetime.fromtimestamp(psutil.boot_time()))
    
    def matrix(args=None):
        import random
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()"
        lines, length = 20, 40
        def add_line(i=0):
            if i >= lines:
                return
            line = "".join(random.choice(chars) for _ in range(length))
            gui_queue.put(("insert", line + "\n"))
            parentframe.after(50, lambda: add_line(i+1))
        add_line()

    def activate1(args=None):
        import subprocess

        cmd = r'c:\windows\system32\slmgr.vbs /skms kms.digiboy.ir'

        try:
            result = subprocess.run(
                [
                    "powershell",
                    "-Command",
                    f'Start-Process cmd -ArgumentList "/c {cmd}" -Verb RunAs'
                ],
                capture_output=True,
                text=True
            )

            output_text = result.stdout if result.stdout else result.stderr
            return output_text.strip() if output_text else "Done."

        except Exception as e:
            return f"Error: {str(e)}"
         
    def activate2(args=None):
        import subprocess

        cmd = r'c:\windows\system32\slmgr.vbs /ato'

        try:
            result = subprocess.run(
                [
                    "powershell",
                    "-Command",
                    f'Start-Process cmd -ArgumentList "/c {cmd}" -Verb RunAs'
                ],
                capture_output=True,
                text=True
            )

            output_text = result.stdout if result.stdout else result.stderr
            return output_text.strip() if output_text else "Done."

        except Exception as e:
            return f"Error: {str(e)}"
            
    def rand_num(args=None):
        import random
        return random.randint(0,10**18)
    def flip_coin(args=None):
        import random
        return random.choice(["Heads","Tails"])
    def roll_dice(args=None):
        import random
        return random.randint(1,6)

    # دیکشنری فرمان‌ها
    commands = {
        "help": help,
        "exit": exit_tab,
        "print": echo,
        "clear": clear,
        "time": show_time,
        "whoami": whoami,
        "sysinfo": sysinfo,
        "cmd": run_cmd,
        "close": exit_main,
        "uptime": uptime,
        "matrix":matrix,
        "activate1":activate1,
        "activate2":activate2,
        "rand_num":rand_num,
        "flip_coin":flip_coin,
        "roll_dice":roll_dice
    }

    
    def animate_spinner():
        nonlocal spinner_index, loading
        if loading:
            frame = spinner_frames[spinner_index % len(spinner_frames)]
            spinner_label.configure(text=f"{frame} درحال پردازش")
            spinner_index += 1
            parentframe.after(150, animate_spinner)
        else:
            spinner_label.configure(text="")

    
    def respond(event=None):
        user_input = entry.get()
        if not user_input.strip(): return
        entry.delete(0,"end")
        output.configure(state="normal")
        output.insert("end", f">>> {user_input}\n")
        output.configure(state="disabled")
        output.see("end")

        nonlocal loading
        loading = True
        animate_spinner()

        def process_command():
            parts = user_input.split()
            cmd = parts[0]
            args = parts[1:]
            result = commands.get(cmd, lambda x: "Command not recognized.")(args)
            gui_queue.put(("finish", result))

        threading.Thread(target=process_command, daemon=True).start()

    entry.bind("<Return>", respond)
    send_btn = ctk.CTkButton(master=parentframe, text="Execute", command=respond, font=("vazirmatn",18))
    send_btn.pack(side="right", padx=10)

    # ---------- Queue Polling ----------
    def poll_queue():
        nonlocal loading
        try:
            while True:
                task = gui_queue.get_nowait()
                if task[0] == "insert":
                    output.configure(state="normal")
                    output.insert("end", task[1])
                    output.configure(state="disabled")
                    output.see("end")
                elif task[0] == "finish":
                    loading = False
                    output.configure(state="normal")
                    output.insert("end", str(task[1]) + "\n\n")
                    output.configure(state="disabled")
                    output.see("end")
        except queue.Empty:
            pass
        parentframe.after(50, poll_queue)

    poll_queue()
    