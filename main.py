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

#section2
frame2 = tb.Frame(root)
frame2.pack(side='bottom',fill='x')