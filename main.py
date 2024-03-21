import tkinter as tk
from tkinter import messagebox
import time
import ctypes

remaining_time = 60 * 60
break_time = 10 * 60
is_paused = False
is_break_time = False

def update_timer():

    global remaining_time, is_break_time

    if remaining_time > 0 and not is_paused:
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
        remaining_time -= 1
        window.after(1000, update_timer)
    elif remaining_time == 0:
        if is_break_time:
            print("Break time finished!")
            is_break_time = False
            ctypes.windll.user32.MessageBoxW(0, "O tempo de pausa terminou. Aperte em OK pra reiniciar o timer principal", "Alerta", 1)
            start_timer()
        else:
            print("Timer finished!")
            is_break_time = True
            ctypes.windll.user32.MessageBoxW(0, "O tempo principal terminou. Aperte em OK pra iniciar o tempo de pausa", "Alerta", 1)
            start_break()

def start_timer():
    global remaining_time, is_paused
    is_paused = False
    update_timer()
    print("Timer started!")

def start_break():
    global remaining_time, is_paused
    remaining_time = break_time
    is_paused = False
    update_timer()
    print("Break time started!")

def pause_timer():
    global is_paused
    is_paused = not is_paused
    if is_paused:
        print("Timer paused!")
    else:
        print("Timer resumed!")
        update_timer()

def reset_timer():
    global remaining_time, is_paused
    is_paused = False
    canvas.itemconfig(timer_text, text=f"{remaining_time // 60:02d}:{remaining_time % 60:02d}")
    print("Timer reset!")

def update_timer_text():
    minutes = remaining_time // 60
    seconds = remaining_time % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")

def open_configuration_window():
    # Create a new window for configuration
    config_window = tk.Toplevel(window)        
    config_window.title("Configuration")
    config_window.geometry("200x150")
    config_window.configure(background="#b22222")

    # Create labels and entry fields for setting the timer and break time
    timer_label = tk.Label(config_window, text="Timer (minutes):",font=("Comic Sans MS", 12), bg="#b22222", fg="white")
    timer_label.pack()
    timer_entry = tk.Entry(config_window, bg="#b22222", fg="white")
    timer_entry.pack()

    break_label = tk.Label(config_window, text="Break (minutes):",font=("Comic Sans MS", 12), bg="#b22222", fg="white")
    break_label.pack()
    break_entry = tk.Entry(config_window, bg="#b22222", fg="white")
    break_entry.pack()

    # Create a save button to apply the configuration
    save_button = tk.Button(config_window, text="Save", command=lambda: save_configuration(timer_entry.get(), break_entry.get()), bg="red", fg="white", font=("Comic Sans MS", 14), width=5, height=1, bd=5, relief="ridge")
    save_button.pack()

def save_configuration(timer, break_duration):
    global remaining_time, break_time
    remaining_time = int(timer) * 60
    break_time = int(break_duration) * 60
    update_timer_text()

window = tk.Tk()
window.title("Pomodoro Timer")
window.minsize(width=500, height=300)
window.configure(background="#b22222")

window.iconbitmap("assets/pomodoro.ico")

label = tk.Label(text="Pomodoro Timer", font=("Comic Sans MS", 24), bg="#b22222", fg="white")
label.grid(row=0, column=1, pady=10)

image = tk.PhotoImage(file="assets/pomodoro.png")
image_label = tk.Label(image=image, bg="#b22222")
image_label.grid(row=1, column=0, rowspan=4)

canvas = tk.Canvas(window, width=500, height=200, bg="#b22222", highlightthickness=0)
canvas.grid(row=1, column=1)

timer_text = canvas.create_text(250, 100, text="60:00", font=("Comic Sans MS", 40, "bold"), fill="white")

start_button = tk.Button(text="Start", highlightthickness=0, command=start_timer, bg="red", fg="white", font=("Comic Sans MS", 14), width=10, height=2, bd=5, relief="ridge")
start_button.grid(row=2, column=1)

reset_button = tk.Button(text="Reset", highlightthickness=0, command=reset_timer, bg="red", fg="white", font=("Comic Sans MS", 14), width=10, height=2, bd=5, relief="ridge")
reset_button.grid(row=3, column=1)

pause_button = tk.Button(text="Pause", highlightthickness=0, command=pause_timer, bg="red", fg="white", font=("Comic Sans MS", 14), width=10, height=2, bd=5, relief="ridge")
pause_button.grid(row=4, column=1)

label = tk.Label(text="Make by: Cayo-Cesar", font=("Comic Sans MS", 10), bg="#b22222", fg="white")
label.grid(row=5, column=1, pady=10)

configure_button = tk.Button(text="Configure", highlightthickness=0, command=open_configuration_window, bg="red", fg="white", font=("Comic Sans MS", 14), width=10, height=2, bd=5, relief="ridge")
configure_button.grid(row=6, column=0)

window.mainloop()
