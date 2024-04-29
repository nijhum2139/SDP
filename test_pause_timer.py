import pytest
from pomodoro import pause_timer
import datetime

timer_start = None
timer_end = None
timer_running = True
timer_mode = "pomodoro"

def pause_timer_button_state():
    pass

def test_pause_timer():
    global timer_running
    current_time = datetime.datetime.now()

    timer_end = datetime.datetime.now() - datetime.timedelta(seconds=10)
    remaining = timer_end - current_time

    pause_timer()

    assert timer_running == True
    assert remaining == timer_end - current_time