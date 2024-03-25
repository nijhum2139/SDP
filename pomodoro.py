import tkinter as tk
import ttkbootstrap as tb
from datetime import datetime, timedelta
import datetime
import main
from main import root

#pomodoro frame
pomodoro_frame = tb.Frame(main.frame1, bootstyle="primary", width=350) #frame for pomodoro
pomodoro_frame.pack(fill="both", expand=True,  padx = 10, pady=10, side='left')

#constants for pomodoro timer
POMODORO_TIME = 25 #time for one session
BREAK_TIME = 5 #break after one session
LONG_BREAK_TIME = 30 #long break after some sessions
POMODORO_SESSION = 4 #sessions per long break

#variables for storing and showing time
time_var = tk.StringVar() #stores time value
time_var.set(f"{POMODORO_TIME}:00")
time_label = tb.Label(pomodoro_frame, textvariable=time_var,font=("Helvetica",48), style="success.TLabel") #For showing time count
time_label.pack(pady=20)

#Status label
status_var = tk.StringVar() #stores the status
status_var.set('Ready to Study?')
status_label = tb.Label(pomodoro_frame, textvariable= status_var, font=("Helvetica",28)) #shows the current status
status_label.pack()

#buttons for pomodoro
start_button = tb.Button(pomodoro_frame,text="START",style="success.Outline.TButton") #button to start timer
start_button.pack(pady=10)
pause_button = tb.Button(pomodoro_frame,text="PAUSE",style="warning.Outline.TButton",state="disabled") #button to pause timer
pause_button.pack(pady=10)
reset_button = tb.Button(pomodoro_frame,text="RESET",style="warning.Outline.TButton",state="disabled") #button to reset timer
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
                update_break_status()
        else:
            update_remaining_time(now)
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


def update_break_status():
    global timer_mode
    start_button["state"] = "normal"
    pause_button["state"] = "disabled"
    reset_button["state"] = "disabled"
    if timer_mode == "break":
        status_var.set("Break completed")
    elif timer_mode == "long break":
        status_var.set("Long break completed")
    timer_mode = "pomodoro"
    time_var.set(f"{BREAK_TIME}:00")


def update_remaining_time(now):
    global timer_end
    remaining = timer_end - now
    minutes = remaining.seconds // 60
    seconds = remaining.seconds % 60
    time_var.set(f"{minutes:02}:{seconds:02}")

#function for starting timer
def start_timer():
    global timer_start, timer_end, timer_running, timer_mode
    if not timer_running:
        timer_start = datetime.now() #store the start time
        if timer_mode == "pomodoro": #if timer is already started
            timer_end = timer_start + timedelta(minutes=POMODORO_TIME) #The timer will stop after this time
            status_var.set(f"Pomodoro session {pomodoro_count +1} running!")
        elif timer_mode == "break": #if it is a break time
            timer_end = timer_start + timedelta(minutes=BREAK_TIME)  # The timer will stop after this time
            status_var.set(f"TIme to take a break!")
        elif timer_mode == "long break": #after 4 sessions
            timer_end = timer_start + timedelta(minutes=LONG_BREAK_TIME)  # The timer will stop after this time
            status_var.set(f" You have earned a long break!")
        timer_running = True
        start_button["state"] = "disabled"  # disable the start button and normalize the pause and reset
        pause_button["state"] = "normal"
        reset_button["state"] = "normal"

def pause_timer():
    global timer_start, timer_end, timer_running, timer_mode
    if timer_running:
        remaining = timer_end - datetime.now() # calculate the remaining time
        minutes = remaining.seconds // 60 # get the remaining minutes
        seconds = remaining.seconds % 60 # get the remaining seconds
        time_var.set(f"{minutes:02}:{seconds:02}") # update the timer value
        timer_running = False # set the timer running to False
        start_button["state"] = "normal" # enable the start button,reset button and disable the pause button
        pause_button["state"] = "disabled"
        reset_button["state"] = "normal"
        status_var.set("Paused")

def reset_timer():
    global timer_start,timer_end,timer_running,timer_mode
    timer_running = False #timer stops
    #button states
    start_button["state"] = "normal"
    pause_button["state"] = "disabled"
    reset_button["state"] = "disabled" #can use only the start button not anything else
    if timer_mode == "pomodoro": #if timer is running
        time_var.set(f"{POMODORO_TIME}:00") #set the running time
        status_var.set(f"Ready to study")
    elif timer_mode == "break": #if it is a break time
        time_var.set(f"{BREAK_TIME}:00")
        status_var.set(f"Pomodoro {pomodoro_count} completed") #shows how many sessions are completed
    elif timer_mode == "long break":
        time_var.set(f"{LONG_BREAK_TIME}:00")  # set the long break time
        status_var.set(f"Pomodoro {pomodoro_count} completed")  # shows how many sessions are completed


#button binding
start_button["command"] = start_timer
pause_button["command"] = pause_timer
reset_button["command"] = reset_timer
