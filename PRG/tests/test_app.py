import pytest
from fastapi.testclient import TestClient
from PRG.app import app

client = TestClient(app)

def test_create_new_user():

    response = client.post(
        "/user",
        json={"username": "testuser", "user_email": "testuser@example.com"},
        follow_redirects=False
    )
    assert response.status_code == 303
    redirected_url = response.headers["Location"]
    assert redirected_url.startswith("/user/")

def test_get_user():
    user_id = 12345
    response = client.get(f"/user/{user_id}")
    assert response.status_code == 200
    assert response.json() == {"user_id": user_id}
