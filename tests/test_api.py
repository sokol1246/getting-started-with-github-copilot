from fastapi.testclient import TestClient

from src.app import activities, app


def test_unregister_participant_removes_email_from_activity():
    client = TestClient(app)
    activity_name = "Chess Club"
    email = "teststudent@mergington.edu"

    activities[activity_name]["participants"].append(email)

    try:
        response = client.delete(f"/activities/{activity_name}/participants/{email}")
        assert response.status_code == 200
        assert email not in activities[activity_name]["participants"]
    finally:
        if email in activities[activity_name]["participants"]:
            activities[activity_name]["participants"].remove(email)


def test_unregister_participant_returns_404_for_unknown_activity():
    client = TestClient(app)

    response = client.delete("/activities/Unknown Activity/participants/test@mergington.edu")

    assert response.status_code == 404
