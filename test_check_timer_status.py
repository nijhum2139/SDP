import datetime
import pytest
from pomodoro import check_timer_status

timer_running = False
timer_end = datetime.datetime.now() + datetime.timedelta(seconds=10)
timer_mode = "pomodoro"
pomodoro_count = 0

def update_pomodoro_status():
    pass

def update_break_status(*args):
    pass

def update_break_status_button():
    pass

def update_remaining_time(*args):
    pass

def test_timer_running():
    global timer_running
    timer_running = True
    check_timer_status()
    assert timer_running == True

def test_timer_pomodoro():
    global timer_mode, pomodoro_count
    timer_mode = "pomodoro"
    check_timer_status()
    assert pomodoro_count == 0

def test_timer_break():
    global timer_mode
    timer_mode = "break"
    check_timer_status()
    assert timer_mode == "break"
