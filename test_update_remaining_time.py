from datetime import timedelta
import pytest
from pomodoro import update_remaining_time

timer_end = timedelta(minutes= 100)
now = timedelta(minutes= 50)

def test_update_remaining_time_sets_time_var():
    class MockTimeVar:
        def set(self, value):
            self.value = value

    time_var = MockTimeVar()

    update_remaining_time(timer_end,now,time_var)

    assert time_var.value == "50:00"

if "__name__" == "__main__":
    pytest.main(["-v", "test_update_remaining_time.py"])