import pytest
import sqlite3
from fastapi.testclient import TestClient
from GenAI_FastApi import app   # <-- make sure your FastAPI file is named main.py
import GenAI_Database

client = TestClient(app)

# Ensure fresh DB before each test
@pytest.fixture(autouse=True)
def setup_and_teardown():
    conn = sqlite3.connect("Task_List.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS Tasks")
    conn.commit()
    conn.close()
    GenAI_Database.init()
    yield


def test_create_task():
    response = client.post("/tasks", json={"title": "First Task"})
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Task added successfully"
    assert data["title"] == "First Task"


def test_list_tasks():
    # Add a task
    client.post("/tasks", json={"title": "Test Task"})
    response = client.get("/tasks/")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) >= 1
    # Title should be at index 1 of tuple
    assert "Test Task" in [t[1] for t in tasks]


def test_mark_completed():
    # Add a task
    client.post("/tasks", json={"title": "Complete Me"})
    tasks = client.get("/tasks/").json()
    task_id = tasks[0][0]

    # Mark completed
    response = client.put(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["completed"] is True

    # Verify in DB
    updated_tasks = client.get("/tasks/").json()
    assert updated_tasks[0][2] == "Completed"


def test_delete_task():
    # Add a task
    client.post("/tasks", json={"title": "Delete Me"})
    tasks = client.get("/tasks/").json()
    task_id = tasks[0][0]

    # Delete task
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Task deleted"

    # Verify it's gone
    remaining = client.get("/tasks/").json()
    assert all(t[0] != task_id for t in remaining)
