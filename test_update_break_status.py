import pytest
from pomodoro import update_break_status

timer_mode1 = "break"
timer_mode2 = "long break"
BREAK_TIME = 5

def test_update_break_status_sets_status_time_var():
    class MockStatusVar:
        def set(self, value):
            self.value = value

    class MockTimeVar:
        def set(self, value):
            self.value = value

    time_var= MockTimeVar()
    status_var = MockStatusVar()

    update_break_status(timer_mode1,status_var,time_var,BREAK_TIME)

    assert time_var.value == "5:00"
    assert status_var.value == "Break completed"
    assert timer_mode1 == "break"

    update_break_status(timer_mode2,status_var,time_var,BREAK_TIME)

    assert time_var.value == "5:00"
    assert status_var.value == "Long break completed"
    assert timer_mode2 == "long break"


if "__name__" == "__main__":
    pytest.main(["-v", "test_update_break_status.py"])


