import psutil
import psutil
import time
import subprocess
import customtkinter
import threading
import tkinter.font as tkf
import queue

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

update_queue = queue.Queue()

def is_running(process_name):
     for proc in psutil.process_iter(['pid', 'name']):
           if proc.info['name'] == process_name:
                return True
     return False

def main():
        while True:
            print(terminate_process('java.exe'))
            print(terminate_process('javaw.exe'))
            is_blocked = True
            time.sleep(60)

def terminate_process(process_name):
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == process_name:
                proc.terminate()
                proc.wait()
                print(f"Prozess {process_name} (PID: {proc.info['pid']}) beendet.")
                return
        print(f"Prozess {process_name} nicht gefunden.")

def start_process(process_path):

    subprocess.Popen(process_path, creationflags=subprocess.CREATE_NO_WINDOW)

def start_Ld_process():
     ld_console= r"C:\Program Files (x86)\LDC\Agent\bin\ldas.exe"
     start_process(ld_console)

root = customtkinter.CTk()
root.geometry("700x600")
font=customtkinter.CTkFont(family='Roboto', size= 24)
font=('Roboto', 24)

root.title("LD Blockapp")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="LD_Block Projekt", font = font)
label.pack(pady=12, padx=10)

status_label = customtkinter.CTkLabel(master=frame, text="Status der LD Konsole", fg_color="gray")
status_label.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="...", command=lambda: None)  # Placeholder-Button
button.pack(pady=10, padx=10)

bold_font = customtkinter.CTkFont(family='Roboto', size=20, weight='bold')

def update_button():
    if is_running('java.exe') or is_running('javaw.exe'):
        
        button.configure(text="Stopp LD_Console", command=lambda: threading.Thread(target=main).start())
        button.pack(pady=20)
        status_label.configure(text="❌LD_Console is aktive!❌", fg_color="red")
    else:
        
        button.configure(text="Start the LD_Console", command=lambda: threading.Thread(target=start_Ld_process).start())
        status_label.configure(text="✅LD_Console is blocked!✅", fg_color="green")

    root.after(1000, update_button)

root.after(100, update_button)

label1 = customtkinter.CTkLabel(master=frame, text="You can close the window now and easily reopen it later!", font=bold_font, wraplength=500)
label1.pack(pady=20, padx=10)

label4 = customtkinter.CTkLabel(master=frame, text="ATTENTION:", fg_color="red", font=bold_font)
label4.pack(pady=12, padx=10)

label2 = customtkinter.CTkLabel(master=frame, text="This program can stop the LD_Console! It's a project created solely for practicing Python programming (code in README.txt). Using it for any other purpose, especially those that might break school rules, is strictly prohibited. Use at your own risk. I am not responsible for any consequences. For educational purposes only!", wraplength=500)
label2.pack(pady=20, padx=10)

labe3 = customtkinter.CTkLabel(master=frame, text="Made By LarZarus")
labe3.pack(pady=20, padx=10)

def run_gui():
    root.mainloop() 

def background_task():
    while True:
        # Hier kannst du deine Hintergrundaufgaben ausführen
        time.sleep(60)
        update_queue.put("Update from background task")   

root.mainloop()
threading.Thread(target=background_task, daemon=True).start()
