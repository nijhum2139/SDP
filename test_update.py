import pytest
from goal import update_goal_list
goals = [
        {"name": "Learn Python", "date": "2024-04-01"},
        {"name": "Exercise daily", "date": "2024-04-02"},
    ]
goals2 =[
        {"name": "Learn java", "date": "2025-04-01"},
        {"name": "Exercise weekly", "date": "2025-04-02"},
    ]
def test_update_goal_list_inserts_goals():
    class MockGoalList:
        def __init__(self):
            self.items = []

        def insert(self, index, item):
            self.items.append(item)

        def delete(self, start, end):
            self.items = []


    goal_list = MockGoalList()

    for goal in goals2:
        goal_list.insert("end", f"{goal['name']} - {goal['date']}")



    update_goal_list(goals,goal_list)

    assert goal_list.items == [
        "Learn Python - 2024-04-01",
        "Exercise daily - 2024-04-02",
    ]

if "__name__" == "__main__":
    pytest.main(["-v", "test_update.py"])
