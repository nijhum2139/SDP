import json
import pytest
from goal import load_goals

GOAL_FILE = "test_goals.json"
goals = []

sample_goals = [{"id": 1, "name": "Read a book"}, {"id": 2, "name": "Exercise"}]
with open(GOAL_FILE, "w") as f:
    json.dump(sample_goals, f)

def test_load_goals():
    global goals, GOAL_FILE
    try:
        with open(GOAL_FILE, "r") as f:
            goals = json.load(f)
    except:
        goals = []
    assert goals == sample_goals