import tkinter as tk
from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap import Style
from datetime import datetime, timedelta
import json

from ttkbootstrap.dialogs import Messagebox
import main
from main import frame1, root



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
