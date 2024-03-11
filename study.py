import goal
import pomodoro
from SDP.syllabus import load_tasks, update_treeview
from main import frame1, root, frame2


pomodoro.update_timer()
goal.load_goals()
load_tasks()
update_treeview()

root.mainloop()