import datetime
import pytest
from pomodoro import start_timer

timer_start = None
timer_end = None
timer_running = False
timer_mode = None
pomodoro_count = 0
POMODORO_TIME = 25 * 60
BREAK_TIME = 5
LONG_BREAK_TIME = 15

def start_timer_button_state():
    pass

def test_start_timer_pomodoro():
    global timer_running, timer_mode, timer_end
    timer_running = False
    timer_mode = "pomodoro"
    start_timer()
    assert timer_running == False
    assert timer_mode == "pomodoro"

def test_start_timer_break():
    global timer_running, timer_mode, timer_end
    timer_running = False
    timer_mode = "break"
    start_timer()
    assert timer_running == False
    assert timer_mode == "break"

def test_start_timer_long_break():
    global timer_running, timer_mode, timer_end
    timer_running = False
    timer_mode = "long break"
    start_timer()
    assert timer_running == False
    assert timer_mode == "long break"
