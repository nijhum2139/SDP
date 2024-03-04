import tkinter as tk
from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap import Style
from datetime import datetime, timedelta
import json

from ttkbootstrap.dialogs import Messagebox

#main window
root = tb.Window(themename="cyborg")
root.title("Syllabus")
root.geometry("700x800")

#section1
frame1 = tb.Frame(root)
frame1.pack(side='top',fill='x')

#pomodoro frame
pomodoro_frame = tb.Frame(frame1, bootstyle="primary", width=350) #frame for pomodoro
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
                time_var.set(f"{BREAK_TIME}:00")
            elif timer_mode == "long break": # if it was a long break
                status_var.set("Long break completed")
                timer_mode = "pomodoro"
                time_var.set(f"{LONG_BREAK_TIME}:00")
        else:
            remaining = timer_end - now
            minutes = remaining.seconds // 60
            seconds = remaining.seconds % 60
            time_var.set(f"{minutes:02}:{seconds:02}")
    root.after(1000, update_timer)

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
        timer_running = True  # set the timer running to True
        start_button["state"] = "disabled"  # disable the start button
        pause_button["state"] = "normal"  # enable the pause button
        reset_button["state"] = "normal"  # enable the reset button

def pause_timer():
    global timer_start, timer_end, timer_running, timer_mode
    if timer_running: # if the timer is running
        remaining = timer_end - datetime.now() # calculate the remaining time
        minutes = remaining.seconds // 60 # get the remaining minutes
        seconds = remaining.seconds % 60 # get the remaining seconds
        time_var.set(f"{minutes:02}:{seconds:02}") # update the timer value
        timer_running = False # set the timer running to False
        start_button["state"] = "normal" # enable the start button
        pause_button["state"] = "disabled" # disable the pause button
        reset_button["state"] = "normal" # enable the reset button
        status_var.set("Paused") # update the status

def reset_timer():
    global timer_start,timer_end,timer_running,timer_mode
    timer_running = False #timer stops
    #button states
    start_button["state"] = "normal"
    pause_button["state"] = "disabled"
    reset_button["state"] = "disabled" #can use only the start button not anything else
    if timer_mode == "pomodoro": #if timer is running
        time_var.set(f"{POMODORO_TIME}:00") #set the running time
        status_var.set(f"Ready to study") #update status
    elif timer_mode == "break": #if it is a break time
        time_var.set(f"{BREAK_TIME}:00") #set the break time
        status_var.set(f"Pomodoro {pomodoro_count} completed") #shows how many sessions are completed
    elif timer_mode == "long break":
        time_var.set(f"{LONG_BREAK_TIME}:00")  # set the long break time
        status_var.set(f"Pomodoro {pomodoro_count} completed")  # shows how many sessions are completed


#button binding
start_button["command"] = start_timer
pause_button["command"] = pause_timer
reset_button["command"] = reset_timer

#calling the update timer function
update_timer()


# Define some constants
GOAL_FILE = "goals.json" # file name to store the goals
HISTORY_FILE = "history.json" #file for storing history
DATE_FORMAT = "%Y-%m-%d" # date format to display and parse

#goalframe
goalframe = tb.Frame(frame1,width=350)
goalframe.pack(side="right",padx = 10, pady=10,expand=True)

# Create the goal listbox
goal_list = tk.Listbox(goalframe, height=300)
goal_list.pack(fill="both", expand=True)

# Create the scrollbar for the goal listbox
goal_scroll = tb.Scrollbar(goal_list, orient="vertical", command=goal_list.yview)
goal_scroll.pack(side="right", fill="y")
goal_list["yscrollcommand"] = goal_scroll.set

# Create the frame to hold the goal entry and buttons
goal_entry_frame = tb.Frame(goalframe)
goal_entry_frame.pack(side="bottom", fill="x")

# Create the goal entry
goal_var = tk.StringVar() # variable to store the goal value
goal_entry = tk.Entry(goal_entry_frame, textvariable=goal_var)
goal_entry.pack(side="left", fill="x", expand=True)

# Create the date entry
date_var = tk.StringVar() # variable to store the date value
date_entry = tk.Entry(goal_entry_frame, textvariable=date_var)
date_entry.pack(side="left", fill="x", expand=True)

#goal buttons frame
goal_button_frame = tb.Frame(goalframe)
goal_button_frame.pack(side="top")

# Create the add, edit, delete, and history buttons
add_button = tb.Button(goal_button_frame, text="Add", style="success.Outline.TButton")
add_button.pack(side="left", padx=5, pady=5)
edit_button = tb.Button(goal_button_frame, text="Edit", style="primary.Outline.TButton")
edit_button.pack(side="left", padx=5, pady=5)
delete_button = tb.Button(goal_button_frame, text="Delete", style="danger.Outline.TButton")
delete_button.pack(side="left", padx=5, pady=5)
history_button = tb.Button(goal_button_frame, text="History", style="info.Outline.TButton")
history_button.pack(side="left", padx=5, pady=5)

# Create the variables to store the goals and history
goals = [] # a list of goals
history = [] # a list of completed goals

# Define the function to load the goals from the file
def load_goals():
    global goals
    try: # try to open the file
        with open(GOAL_FILE, "r") as f: # open the file in read mode
            goals = json.load(f) # load the goals as a list
    except: # if the file does not exist or is corrupted
        goals = [] # set the goals to an empty list

# Define the function to save the goals to the file
def save_goals():
    global goals
    try: # try to open the file
        with open(GOAL_FILE, "w") as f: # open the file in write mode
            json.dump(goals, f) # dump the goals as a list
    except: # if the file cannot be opened or written
        pass # do nothing

# Define the function to update the goal listbox
def update_goal_list():
    global goals
    goal_list.delete(0, "end") # delete all the items in the listbox
    for goal in goals: # for each goal in the goals list
        goal_list.insert("end", f"{goal['name']} - {goal['date']}") # insert the goal to the listbox

# Define the function to add a goal
def add_goal():
    global goals,date
    goal = goal_var.get() # get the goal value from the entry
    date = date_var.get() # get the date value from the entry
    if goal and date: # if the goal and date are not empty
        try: # try to parse the date
            date_obj = datetime.strptime(date, DATE_FORMAT) # parse the date as a datetime object
            date_str = date_obj.strftime(DATE_FORMAT) # format the date as a string
            goals.append({"name": goal, "date": date_str}) # append the goal to the goals list
            save_goals() # save the goals to the file
            update_goal_list() # update the goal listbox
            goal_var.set("") # clear the goal entry
            date_var.set("") # clear the date entry
            goal_entry.focus() # focus on the goal entry
        except: # if the date is invalid
            Messagebox.show_error("Invalid date format. Please use YYYY-MM-DD.", "Error") # show an error message

# Define the function to edit a goal
def edit_goal():
    global goals,date
    goal = goal_var.get() # get the goal value from the entry
    date = date_var.get() # get the date value from the entry
    index = goal_list.curselection() # get the index of the selected item in the listbox
    if goal and date and index: # if the goal, date, and index are not empty
        try: # try to parse the date
            date_obj = datetime.strptime(date, DATE_FORMAT) # parse the date as a datetime object
            date_str = date_obj.strftime(DATE_FORMAT) # format the date as a string
            goals[index[0]] = {"name": goal, "date": date_str} # update the goal in the goals list
            save_goals() # save the goals to the file
            update_goal_list() # update the goal listbox
            goal_var.set("") # clear the goal entry
            date_var.set("") # clear the date entry
            goal_entry.focus() # focus on the goal entry
        except: # if the date is invalid
            Messagebox.show_error("Invalid date format. Please use YYYY-MM-DD.", "Error") # show an error message

# Define the function to delete a goal
def delete_goal():
    global goals
    index = goal_list.curselection() # get the index of the selected item in the listbox
    if index: # if an item is selected
        goals.pop(index[0]) # remove the goal from the goals list
        save_goals() # save the goals to the file
        update_goal_list() # update the goal listbox
        goal_var.set("") # clear the goal entry
        date_var.set("") # clear the date entry
        goal_entry.focus() # focus on the goal entry

# Define the function to save the history to the file
def save_history():
    global history
    try: # try to open the file
        with open(HISTORY_FILE, "w") as f: # open the file in write mode
            json.dump(history, f) # dump the goals as a list
    except: # if the file cannot be opened or written
        pass # do nothing

# Define the function to load the goals from the file
def load_history():
    global history
    try: # try to open the file
        with open(HISTORY_FILE, "r") as f: # open the file in read mode
            history = json.load(f) # load the goals as a list
    except: # if the file does not exist or is corrupted
        history = [] # set the goals to an empty list

# Define the function to mark a goal as completed
def complete_goal():
    global goals, history
    index = goal_list.curselection() # get the index of the selected item in the listbox
    if index: # if an item is selected
        goal = goals.pop(index[0]) # remove the goal from the goals list
        history.append(goal) # append the goal to the history list
        save_history() #save the history
        save_goals() # save the goals to the file
        update_goal_list() # update the goal listbox
        goal_var.set("") # clear the goal entry
        date_var.set("") # clear the date entry
        goal_entry.focus() # focus on the goal entry

# Define the function to show the history of completed goals
def show_history():
    global history
    history_window = tk.Toplevel(root) # create a new window
    history_window.title("Goal History") # set the window title
    history_window.geometry("300x200") # set the window size
    history_list = tk.Listbox(history_window, height=10) # create a listbox to show the history
    history_list.pack(side="left", fill="both", expand=True) # pack the listbox
    history_scroll = tk.Scrollbar(history_window, orient="vertical", command=history_list.yview) # create a scrollbar for the listbox
    history_scroll.pack(side="right", fill="y") # pack the scrollbar
    history_list["yscrollcommand"] = history_scroll.set # link the listbox and the scrollbar
    for goal in history: # for each goal in the history list
        history_list.insert("end", f"{goal['name']} - {goal['date']}") # insert the goal to the listbox

# Bind the functions to the buttons
add_button["command"] = add_goal
edit_button["command"] = edit_goal
delete_button["command"] = delete_goal
history_button["command"] = show_history

# Bind the function to mark a goal as completed to the double click event on the listbox
goal_list.bind("<Double-Button-1>", lambda x: complete_goal())

# Bind the function to add a goal to the return key event on the entry
goal_entry.bind("<Return>", lambda x: add_goal())

# Load the goals from the file
load_goals()

#load the history from the file
load_history()

# Update the goal listbox for the first time
update_goal_list()

# def add_syllabus():
#     f = open("mysyllabus.txt","a")
#     f.write(f"{sub_text.get()}\n")
#     f.close()
#     f = open("mysyllabus.txt", "r")
#     my_label.config(text=f.read())
#     f.close()
#
#
#
#
# subject = tb.Label(text="Subject name: ", font=("Helvetica",20), bootstyle = SUCCESS)
# subject.pack(padx=10,pady=20)
#
# sub_text = tb.Entry()
# sub_text.pack(padx=20)
#
# topic = tb.Label(text="Number of topics: ", font=("Helvetica",20), bootstyle = "warning")
# topic.pack(padx=10,pady=20)
#
# topic_text = tb.Entry()
# topic_text.pack(padx=20)
#
# add_button = tb.Button(text="ADD", bootstyle=SUCCESS, command=add_syllabus)
# add_button.pack(pady=30)
#
#
# f = open("mysyllabus.txt","r")
# my_label = tb.Label(text=f.read(), font=("Helvetica",20))
# my_label.pack(pady=20)
# f.close()

root.mainloop()