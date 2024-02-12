import tkinter as tk
from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap import Style
from datetime import datetime, timedelta



#main window
root = tb.Window(themename="cyborg")
root.title("Syllabus")
root.geometry("700x800")


#pomodoro frame
pomodoro_frame = tb.Frame(root) #frame for pomodoro
pomodoro_frame.pack(fill="both", expand=True)

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


#function for starting timer
def start_timer():
    global timer_start, timer_end, timer_running, timer_mode
    if not timer_running: #if the timer is not running
        timer_start = datetime.now() #store the start time
        if timer_mode == "pomodoro": #if timer is already started
            timer_end = timer_start + timedelta(minutes=POMODORO_TIME) #The timer will stop after this time
            status_var.set(f"Pomodoro session {pomodoro_count +1} running!") #showing status
        elif timer_mode == "break": #if it is a break time
            timer_end = timer_start + timedelta(minutes=BREAK_TIME)  # The timer will stop after this time
            status_var.set(f"TIme to take a break!")  # showing status
        elif timer_mode == "long break": #after 4 sessions
            timer_end = timer_start + timedelta(minutes=LONG_BREAK_TIME)  # The timer will stop after this time
            status_var.set(f" You have earned a long break!")  # showing status
        timer_running = True #timer has started
        start_button["state"] = "disabled" #start button is unoperatable
        pause_button["state"] = "normal" #pause button now operational
        reset_button["state"] = "normal" #reset button now operational


















def add_syllabus():
    f = open("mysyllabus.txt","a")
    f.write(f"{sub_text.get()}\n")
    f.close()
    f = open("mysyllabus.txt", "r")
    my_label.config(text=f.read())
    f.close()




subject = tb.Label(text="Subject name: ", font=("Helvetica",20), bootstyle = SUCCESS)
subject.pack(padx=10,pady=20)

sub_text = tb.Entry()
sub_text.pack(padx=20)

topic = tb.Label(text="Number of topics: ", font=("Helvetica",20), bootstyle = "warning")
topic.pack(padx=10,pady=20)

topic_text = tb.Entry()
topic_text.pack(padx=20)

add_button = tb.Button(text="ADD", bootstyle=SUCCESS, command=add_syllabus)
add_button.pack(pady=30)


f = open("mysyllabus.txt","r")
my_label = tb.Label(text=f.read(), font=("Helvetica",20))
my_label.pack(pady=20)
f.close()


root.mainloop()