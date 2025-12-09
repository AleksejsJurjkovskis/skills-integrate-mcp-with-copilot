import copy
from urllib.parse import quote

import pytest

from src.app import app, activities
from fastapi.testclient import TestClient


@pytest.fixture(autouse=True)
def restore_activities():
    """Restore the in-memory activities after each test."""
    original = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(original)


def test_get_activities():
    client = TestClient(app)
    resp = client.get("/activities")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data


def test_signup_and_unregister():
    client = TestClient(app)
    activity = "Chess Club"
    email = "pytest-user@example.test"

    # Sign up
    url = f"/activities/{quote(activity)}/signup"
    resp = client.post(url, params={"email": email})
    assert resp.status_code == 200
    assert email in activities[activity]["participants"]

    # Unregister
    url = f"/activities/{quote(activity)}/unregister"
    resp = client.delete(url, params={"email": email})
    assert resp.status_code == 200
    assert email not in activities[activity]["participants"]
