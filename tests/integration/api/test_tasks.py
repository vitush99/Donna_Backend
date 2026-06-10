import pytest
from fastapi.testclient import TestClient

from donna.domains.tasks.router import task_repository
from donna.main import app


@pytest.fixture(autouse=True)
def clear_tasks() -> None:
    task_repository.clear()


client = TestClient(app)


def test_create_task() -> None:
    response = client.post(
        "/api/tasks",
        json={
            "title": "Finish Phase A",
            "description": "Implement the task API",
        },
    )

    assert response.status_code == 201

    body = response.json()
    assert body["title"] == "Finish Phase A"
    assert body["status"] == "pending"
    assert body["source"] == "manual"
    assert "id" in body
    assert "createdAt" in body
    assert "updatedAt" in body


def test_list_tasks() -> None:
    created = client.post("/api/tasks", json={"title": "List this task"}).json()

    response = client.get("/api/tasks")

    assert response.status_code == 200
    assert response.json() == {"items": [created]}


def test_get_task_by_id() -> None:
    created = client.post("/api/tasks", json={"title": "Find this task"}).json()

    response = client.get(f"/api/tasks/{created['id']}")

    assert response.status_code == 200
    assert response.json() == created


def test_update_task() -> None:
    created = client.post(
        "/api/tasks",
        json={"title": "Original title", "description": "Original description"},
    ).json()

    response = client.patch(
        f"/api/tasks/{created['id']}",
        json={
            "title": "Updated title",
            "description": "Updated description",
            "status": "completed",
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["title"] == "Updated title"
    assert body["description"] == "Updated description"
    assert body["status"] == "completed"
    assert body["updatedAt"] != created["updatedAt"]


def test_get_missing_task_returns_clean_404() -> None:
    response = client.get("/api/tasks/does-not-exist")

    assert response.status_code == 404
    assert response.json() == {
        "error": {
            "code": "not_found",
            "message": "Task not found",
        }
    }


def test_create_task_without_title_returns_clean_400() -> None:
    response = client.post("/api/tasks", json={})

    assert response.status_code == 400
    body = response.json()
    assert body["error"]["code"] == "validation_error"
    assert body["error"]["message"] == "Invalid request body"
    assert body["error"]["details"]


def test_update_task_with_invalid_status_returns_clean_400() -> None:
    created = client.post("/api/tasks", json={"title": "Validate status"}).json()

    response = client.patch(
        f"/api/tasks/{created['id']}",
        json={"status": "not-a-real-status"},
    )

    assert response.status_code == 400
    assert response.json()["error"]["code"] == "validation_error"


def test_unknown_route_returns_clean_404() -> None:
    response = client.get("/not-a-real-route")

    assert response.status_code == 404
    assert response.json() == {
        "error": {
            "code": "route_not_found",
            "message": "Route not found",
        }
    }
