import goal
import pomodoro
from syllabus import load_tasks, update_treeview
from main import frame1, root, frame2


pomodoro.check_timer_status()
pomodoro.update_pomodoro_status()
pomodoro.update_break_status()
pomodoro.update_remaining_time()
goal.load_goals()
load_tasks()
update_treeview()

root.mainloop()