import pytest
from syllabus import save_tasks

tasks = {
    "Task 1": {"status": "Incomplete", "completion_date": "2024-03-31"},
    "Task 2": {"status": "Complete", "completion_date": "2024-03-30"},
}

def test_save_tasks(tmp_path):
    test_file = tmp_path / "test_tasks.txt"
    save_tasks(test_file,tasks)

    with open(test_file, "r") as file:
        saved_content = file.read()

    # Check if the saved content matches the expected format
    expected_content = """Task 1::Incomplete::2024-03-31::
Task 2::Complete::2024-03-30::
"""
    assert saved_content == expected_content

# Run the test
if __name__ == "__main__":
    pytest.main(["-v", "test_tasks.py"])
