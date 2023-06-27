import tkinter as tk
import os
import subprocess
from PIL import ImageTk, Image

current_dir = os.path.dirname(os.path.abspath(__file__))

def open_generator():
    generator_start_button.place(relx=0.35, rely=0.8)
    generator_stop_button.place(relx=0.55, rely=0.8)

def start_generator():
    global generator_process
    generator_path = os.path.join(current_dir, "generator.py")
    generator_process = subprocess.Popen(["python", generator_path], cwd=current_dir)

def stop_generator():
    global generator_process
    if generator_process is not None:
        generator_process.kill()

def open_loginer():
    loginer_start_button.place(relx=0.35, rely=0.8)
    loginer_stop_button.place(relx=0.55, rely=0.8)

def start_loginer():
    global loginer_process
    loginer_path = os.path.join(current_dir, "loginer.py")
    loginer_process = subprocess.Popen(["python", loginer_path], cwd=current_dir)

def stop_loginer():
    global loginer_process
    if loginer_process is not None:
        loginer_process.kill()

def open_validator():
    validator_start_button.place(relx=0.35, rely=0.8)
    validator_stop_button.place(relx=0.55, rely=0.8)

def start_validator():
    global validator_process
    validator_path = os.path.join(current_dir, "validator.py")
    validator_process = subprocess.Popen(["python", validator_path], cwd=current_dir)

def stop_validator():
    global validator_process
    if validator_process is not None:
        validator_process.kill()

def button_click_wrapper(button_number):
    global selected_button
    if selected_button is not None:
        buttons[selected_button].config(relief=tk.RAISED)
        buttons[selected_button].config(bg="black")

    buttons[button_number].config(relief=tk.SUNKEN)
    buttons[button_number].config(bg="gray")
    selected_button = button_number

    if button_number == 4:
        show_accounts()
    else:
        hide_accounts()

    if button_number == 1:
        open_generator()
    else:
        generator_start_button.place_forget()
        generator_stop_button.place_forget()
    
    if button_number == 2:
        open_loginer()
    else:
        loginer_start_button.place_forget()
        loginer_stop_button.place_forget()

    if button_number == 3:
        open_validator()
    else:
        validator_start_button.place_forget()
        validator_stop_button.place_forget()

def show_accounts():
    accounts_file1 = os.path.join(current_dir, "accounts.txt")
    accounts_file2 = os.path.join(current_dir, "verified_accounts.txt")
    accounts_file3 = os.path.join(current_dir, "used_accounts.txt")

    with open(accounts_file1, "r") as f:
        accounts1 = f.read()

    with open(accounts_file2, "r") as f:
        accounts2 = f.read()

    with open(accounts_file3, "r") as f:
        accounts3 = f.read()

    accounts_text1.delete("1.0", tk.END)
    accounts_text1.insert(tk.END, f"Accounts:\n{accounts1}\n\n")
    accounts_text1.place(relx=0.1, rely=0.115, relwidth=0.8, relheight=0.2)

    accounts_text2.delete("1.0", tk.END)
    accounts_text2.insert(tk.END, f"Verified Accounts:\n{accounts2}\n\n")
    accounts_text2.place(relx=0.1, rely=0.415, relwidth=0.8, relheight=0.2)

    accounts_text3.delete("1.0", tk.END)
    accounts_text3.insert(tk.END, f"Used Accounts:\n{accounts3}\n\n")
    accounts_text3.place(relx=0.1, rely=0.715, relwidth=0.8, relheight=0.2)

def hide_accounts():
    accounts_text1.place_forget()
    accounts_text2.place_forget()
    accounts_text3.place_forget()

window = tk.Tk()
window.geometry("600x400")
window.configure(bg="black")
window.title("Steam Tools")

# Arka plan fotoğrafı eklenir
background_image = Image.open(r"C:\Users\Kerem\Desktop\St34m Tools\apparkaplan.png")
window_width = window.winfo_screenwidth()
window_height = window.winfo_screenheight()
background_image = background_image.resize((window_width, window_height), Image.ANTIALIAS)
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

button_frame = tk.Frame(window, bg="black")
button_frame.pack()

button_width = 600 // 5
button_height = 2

buttons = []
selected_button = None

def button_click(button_number):
    button_click_wrapper(button_number)

button_names = ["Steam Tools", "Generator", "Loginer", "Validator", "Accounts"]

for i in range(5):
    button = tk.Button(button_frame, text=button_names[i], command=lambda x=i: button_click(x), fg="white", bg="black", width=button_width, height=button_height)
    button.grid(row=0, column=i, sticky="nsew")
    buttons.append(button)

generator_start_button = tk.Button(window, text="Start", width=10, fg="white", bg="#3F51B5", command=start_generator)
generator_stop_button = tk.Button(window, text="Stop", width=10, fg="white", bg="#FF4081", command=stop_generator)

loginer_start_button = tk.Button(window, text="Start", width=10, fg="white", bg="#3F51B5", command=start_loginer)
loginer_stop_button = tk.Button(window, text="Stop", width=10, fg="white", bg="#FF4081", command=stop_loginer)

validator_start_button = tk.Button(window, text="Start", width=10, fg="white", bg="#3F51B5", command=start_validator)
validator_stop_button = tk.Button(window, text="Stop", width=10, fg="white", bg="#FF4081", command=stop_validator)

accounts_text1 = tk.Text(window, width=60, height=7, fg="white", bg="black")
accounts_text2 = tk.Text(window, width=60, height=7, fg="white", bg="black")
accounts_text3 = tk.Text(window, width=60, height=6.4, fg="white", bg="black")

button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)
button_frame.grid_columnconfigure(2, weight=1)
button_frame.grid_columnconfigure(3, weight=1)
button_frame.grid_columnconfigure(4, weight=1)

window.mainloop()
