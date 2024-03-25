import ttkbootstrap as tb


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