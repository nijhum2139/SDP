import tkinter as tk
import ttkbootstrap as tb
from datetime import datetime
import json
from ttkbootstrap.dialogs import Messagebox
from main import frame1, root

# Define some constants
GOAL_FILE = "goals.json"
HISTORY_FILE = "history.json"
DATE_FORMAT = "%Y-%m-%d"

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
goal_var = tk.StringVar()
goal_entry = tk.Entry(goal_entry_frame, textvariable=goal_var)
goal_entry.pack(side="left", fill="x", expand=True)

# Create the date entry
date_var = tk.StringVar()
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

goals = []
history = []

# Define the function to load the goals from the file
def load_goals():
    global goals,GOAL_FILE
    try:
        with open(GOAL_FILE, "r") as f:
            goals = json.load(f)
    except:
        goals = []

# Define the function to save the goals to the file
def save_goals():
    global goals
    try:
        with open(GOAL_FILE, "w") as f:
            json.dump(goals, f)
    except:
        pass

# Define the function to update the goal listbox
def update_goal_list(goals, goal_list):
    # global goals
    goal_list.delete(0, "end")
    for goal in goals:
        goal_list.insert("end", f"{goal['name']} - {goal['date']}")

# Define the function to add a goal
def add_goal():
    global goals,date
    goal = goal_var.get()
    date = date_var.get()
    if goal and date:
        try:
            date_obj = datetime.strptime(date, DATE_FORMAT)
            date_str = date_obj.strftime(DATE_FORMAT)
            goals.append({"name": goal, "date": date_str})
            save_goals()
            update_goal_list(goals, goal_list)
            goal_var.set("")
            date_var.set("")
            goal_entry.focus()
        except:
            Messagebox.show_error("Invalid date format. Please use YYYY-MM-DD.", "Error")

# Define the function to edit a goal
def edit_goal():
    global goals,date
    goal = goal_var.get()
    date = date_var.get()
    index = goal_list.curselection()
    if goal and date and index:
        try:
            date_obj = datetime.strptime(date, DATE_FORMAT)
            date_str = date_obj.strftime(DATE_FORMAT)
            goals[index[0]] = {"name": goal, "date": date_str}
            save_goals()
            update_goal_list(goals, goal_list)
            goal_var.set("")
            date_var.set("")
            goal_entry.focus()
        except:
            Messagebox.show_error("Invalid date format. Please use YYYY-MM-DD.", "Error")

# Define the function to delete a goal
def delete_goal():
    global goals
    index = goal_list.curselection()
    if index:
        goals.pop(index[0])
        save_goals()
        update_goal_list(goals, goal_list)
        goal_var.set("")
        date_var.set("")
        goal_entry.focus()

# Define the function to save the history to the file
def save_history():
    global history
    try:
        with open(HISTORY_FILE, "w") as f:
            json.dump(history, f)
    except:
        pass

# Define the function to load the goals from the file
def load_history():
    global history
    try:
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    except:
        history = []

# Define the function to mark a goal as completed
def complete_goal():
    global goals, history
    index = goal_list.curselection()
    if index:
        goal = goals.pop(index[0])
        history.append(goal)
        save_history()
        save_goals()
        update_goal_list(goals, goal_list)
        goal_var.set("")
        date_var.set("")
        goal_entry.focus()

# Define the function to show the history of completed goals
def show_history():
    global history
    load_history()
    history_window = tk.Toplevel(root)
    history_window.title("Goal History")
    history_window.geometry("300x200")
    history_list = tk.Listbox(history_window, height=10)
    history_list.pack(side="left", fill="both", expand=True)
    history_scroll = tk.Scrollbar(history_window, orient="vertical", command=history_list.yview)
    history_scroll.pack(side="right", fill="y")
    history_list["yscrollcommand"] = history_scroll.set
    for goal in history:
        history_list.insert("end", f"{goal['name']} - {goal['date']}")

# Bind the functions to the buttons
add_button["command"] = add_goal
edit_button["command"] = edit_goal
delete_button["command"] = delete_goal
history_button["command"] = show_history

# Bind the function to mark a goal as completed to the double click event on the listbox
goal_list.bind("<Double-Button-1>", lambda x: complete_goal())

# Bind the function to add a goal to the return key event on the entry
goal_entry.bind("<Return>", lambda x: add_goal())

