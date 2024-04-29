import tkinter as tk
import ttkbootstrap as tb
from datetime import datetime, timedelta
import datetime
import main
from main import root

#pomodoro frame
pomodoro_frame = tb.Frame(main.frame1, bootstyle="primary", width=350)
pomodoro_frame.pack(fill="both", expand=True,  padx = 10, pady=10, side='left')

POMODORO_TIME = 10
BREAK_TIME = 5
LONG_BREAK_TIME = 30
POMODORO_SESSION = 4

#variables for storing and showing time
time_var = tk.StringVar()
time_var.set(f"{POMODORO_TIME}:00")
time_label = tb.Label(pomodoro_frame, textvariable=time_var,font=("Helvetica",48), style="success.TLabel")
time_label.pack(pady=20)

#Status label
status_var = tk.StringVar()
status_var.set('Ready to Study?')
status_label = tb.Label(pomodoro_frame, textvariable= status_var, font=("Helvetica",28))
status_label.pack()

#buttons for pomodoro
start_button = tb.Button(pomodoro_frame,text="START",style="success.Outline.TButton")
start_button.pack(pady=10)
pause_button = tb.Button(pomodoro_frame,text="PAUSE",style="warning.Outline.TButton",state="disabled")
pause_button.pack(pady=10)
reset_button = tb.Button(pomodoro_frame,text="RESET",style="warning.Outline.TButton",state="disabled")
reset_button.pack(pady=10)

#time keeping variables
timer_start = None
timer_end = None
timer_running = False
timer_mode = "pomodoro"
pomodoro_count = 0



def check_timer_status():
    global timer_running, timer_end, timer_mode, pomodoro_count
    if timer_running:
        now = datetime.datetime.now()
        if now >= timer_end:
            timer_running = False
            if timer_mode == "pomodoro":
                pomodoro_count += 1
                update_pomodoro_status()
            else:
                timer_mode = update_break_status(timer_mode,status_var,time_var,BREAK_TIME)
                update_break_status_button()
        else:
            update_remaining_time(timer_end,now,time_var)
    root.after(1000, check_timer_status)


def update_pomodoro_status():
    global timer_mode
    start_button["state"] = "normal"
    pause_button["state"] = "disabled"
    reset_button["state"] = "disabled"
    status_var.set(f"Pomodoro {pomodoro_count} completed")
    if pomodoro_count % POMODORO_SESSION == 0:
        timer_mode = "long break"
        time_var.set(f"{LONG_BREAK_TIME}:00")
    else:
        timer_mode = "break"
        time_var.set(f"{BREAK_TIME}:00")


def update_break_status(timer_mode,status_var,time_var,BREAK_TIME):
    if timer_mode == "break":
        status_var.set("Break completed")
    elif timer_mode == "long break":
        status_var.set("Long break completed")
    time_var.set(f"{BREAK_TIME}:00")
    timer_mode = "pomodoro"
    return timer_mode

def update_break_status_button():
    start_button["state"] = "normal"
    pause_button["state"] = "disabled"
    reset_button["state"] = "disabled"


def update_remaining_time(timer_end,now,time_var):
    remaining = timer_end - now
    minutes = remaining.seconds // 60
    seconds = remaining.seconds % 60
    time_var.set(f"{minutes:02}:{seconds:02}")

#function for starting timer
def start_timer():
    global timer_start, timer_end, timer_running, timer_mode
    if not timer_running:
        timer_start = datetime.datetime.now()
        if timer_mode == "pomodoro":
            timer_end = timer_start + timedelta(seconds=POMODORO_TIME)
            status_var.set(f"Pomodoro session {pomodoro_count +1} running!")
        elif timer_mode == "break":
            timer_end = timer_start + timedelta(minutes=BREAK_TIME)
            status_var.set(f"TIme to take a break!")
        elif timer_mode == "long break":
            timer_end = timer_start + timedelta(minutes=LONG_BREAK_TIME)
            status_var.set(f" You have earned a long break!")
        timer_running = True
        start_timer_button_state()

def start_timer_button_state():
    start_button["state"] = "disabled"
    pause_button["state"] = "normal"
    reset_button["state"] = "normal"

def pause_timer():
    global timer_start, timer_end, timer_running, timer_mode
    if timer_running:
        remaining = timer_end - datetime.datetime.now()
        minutes = remaining.seconds // 60
        seconds = remaining.seconds % 60
        time_var.set(f"{minutes:02}:{seconds:02}")
        timer_running = False
        pause_timer_button_state()
        status_var.set("Paused")

def pause_timer_button_state():
    start_button["state"] = "normal"
    pause_button["state"] = "disabled"
    reset_button["state"] = "normal"

#this function resets the timer to 0
def reset_timer():
    global timer_start,timer_end,timer_running,timer_mode
    timer_running = False
    start_button["state"] = "normal"
    pause_button["state"] = "disabled"
    reset_button["state"] = "disabled"
    if timer_mode == "pomodoro":
        time_var.set(f"{POMODORO_TIME}:00")
        status_var.set(f"Ready to study")
    elif timer_mode == "break":
        time_var.set(f"{BREAK_TIME}:00")
        status_var.set(f"Pomodoro {pomodoro_count} completed")
    elif timer_mode == "long break":
        time_var.set(f"{LONG_BREAK_TIME}:00")
        status_var.set(f"Pomodoro {pomodoro_count} completed")


#button binding
start_button["command"] = start_timer
pause_button["command"] = pause_timer
reset_button["command"] = reset_timer


check_timer_status()
root.mainloop()