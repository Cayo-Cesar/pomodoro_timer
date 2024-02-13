import tkinter as tk, messagebox
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
    remaining_time = 60 * 60
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
    remaining_time = 60 * 60
    is_paused = False
    canvas.itemconfig(timer_text, text="01:00")
    print("Timer reset!")

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

label = tk.Label(text="Made by: Cayo-Cesar", font=("Comic Sans MS", 10), bg="#b22222", fg="white")
label.grid(row=5, column=1, pady=10)

window.mainloop()
