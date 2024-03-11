import tkinter as tk
from tkinter import ttk, simpledialog
from ttkbootstrap import Style
from datetime import datetime

from main import frame2

tree = ttk.Treeview(frame2, columns=("Topic", "Status", "Completion Date"), show="headings", selectmode="browse")
tree.heading("Task", text="Task")
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




