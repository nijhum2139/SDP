from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *

root = tb.Window(themename="cyborg")
root.title("Syllabus")
root.geometry("1000x850")


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



root.mainloop()