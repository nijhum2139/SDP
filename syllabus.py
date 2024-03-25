import tkinter as tk
from tkinter import ttk, simpledialog
from ttkbootstrap import Style
from datetime import datetime

from main import frame2,root

tree = ttk.Treeview(frame2, columns=("Task", "Status", "Completion Date"), show="headings", selectmode="browse")
tree.heading("Task", text="Topic")
tree.heading("Status", text="Status")

tree.heading("Completion Date", text="Completion Date")
tree.column("Task", anchor="center", width=150)
tree.column("Status", anchor="center", width=80)
tree.column("Completion Date", anchor="center", width=200)
tree.grid(row=0, column=0, padx=10, pady=10)

add_task_button = ttk.Button(frame2, text="Add")
add_task_button.grid(row=1, column=0, pady=5)

delete_task_button = ttk.Button(frame2, text="Delete")
delete_task_button.grid(row=1, column=1, pady=5)

edit_task_button = ttk.Button(frame2, text="Edit")
edit_task_button.grid(row=1, column=2, pady=5)

mark_completed_button = ttk.Button(frame2, text="Mark Completed")
mark_completed_button.grid(row=1, column=3, pady=5)

progress_label = ttk.Label(frame2, text="Progress: 0%")
progress_label.grid(row=2, column=0, pady=5, columnspan=4)

tasks = {}

def add_task():
    task_name = simpledialog.askstring("Input", "Enter task name:")
    if task_name:
        tasks[task_name] = {"status": "Incomplete", "completion_date": None}
        update_treeview()
        save_tasks()

def delete_task():
    selected_item = tree.selection()
    if selected_item:
        task_name = tree.item(selected_item, "values")[0]
        del tasks[task_name]
        update_treeview()
        save_tasks()

def edit_task():
    selected_item = tree.selection()
    if selected_item:
        task_name = tree.item(selected_item, "values")[0]
        edited_name = simpledialog.askstring("Edit Task", "Edit task name:", initialvalue=task_name)
        if edited_name and edited_name != task_name:
            tasks[edited_name] = tasks.pop(task_name)
            update_treeview()
            save_tasks()

def mark_completed():
    selected_item = tree.selection()
    if selected_item:
        task_name = tree.item(selected_item, "values")[0]
        tasks[task_name]["status"] = "Completed"
        tasks[task_name]["completion_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        update_treeview()
        save_tasks()

def update_treeview():
    tree.delete(*tree.get_children())

    for task, details in tasks.items():
        task_completion_status = details["status"]
        completion_date = details["completion_date"] if details["completion_date"] else ""
        tree.insert("", "end", values=(task, task_completion_status, completion_date))
    save_tasks()
    calculate_progress()

def calculate_progress():
    total_tasks = len(tasks)
    completed_tasks = sum(1 for details in tasks.values() if details["status"] == "Completed")
    progress_percentage = 0 if total_tasks == 0 else (completed_tasks / total_tasks) * 100
    progress_label["text"] = f"Progress: {progress_percentage:.2f}%"

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task, details in tasks.items():
            file.write(f"{task}::{details['status']}::{details['completion_date']}::\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split("::")
                task_name, task_status, completion_date = data[0], data[1], data[2]
                tasks[task_name] = {"status": task_status, "completion_date": completion_date}
    except FileNotFoundError:
        pass

add_task_button["command"] = add_task
delete_task_button["command"] = delete_task
edit_task_button["command"] = edit_task
mark_completed_button["command"] = mark_completed

load_tasks()
update_treeview()
root.mainloop()


