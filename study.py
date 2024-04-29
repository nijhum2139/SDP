import goal
import pomodoro
from main import root
import syllabus

pomodoro.check_timer_status()
goal.load_goals()
syllabus.load_tasks()
syllabus.update_treeview()
root.mainloop()