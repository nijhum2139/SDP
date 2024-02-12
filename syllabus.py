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

#time keeping variables
timer_start = None
timer_end = None
timer_running = False
timer_mode = "pomodoro"
pomodoro_count = 0

def update_timer():
    global timer_start, timer_end, timer_running, timer_mode, pomodoro_count
    if timer_running: # if the timer is running
        now = datetime.now() #registers presents time
        if now >= timer_end: #the time is over
            timer_running = False # the timer stops
            start_button["state"] = "normal"
            pause_button["state"] = "disabled"
            reset_button["state"] = "disabled" #only start button is operational
            if timer_mode == "pomodoro": # session on going
                pomodoro_count += 1
                status_var.set(f"Pomodoro {pomodoro_count} completed")
                if pomodoro_count % POMODORO_SESSION == 0: # checking if it is break or long break
                    timer_mode = "long break"
                    time_var.set(f"{LONG_BREAK_TIME}:00")
                else:
                    timer_mode = "break"
                    time_var.set(f"{BREAK_TIME}:00")
            elif timer_mode == "break": # if it was a break
                status_var.set("Break completed")
                timer_mode = "pomodoro"
                time_var.set(f"{POMODORO_TIME}:00")
            elif timer_mode == "long break": # if it was a long break
                status_var.set("Long break completed")
                timer_mode = "pomodoro"
                time_var.set(f"{POMODORO_TIME}:00")
            else:
                remaining = timer_end - now
                minutes = remaining.seconds // 60
                seconds = remaining.seconds % 60
                time_var.set(f"{minutes:02}:{seconds:02}")
            root.after(1000, update_timer)

















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