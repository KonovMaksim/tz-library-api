def test_register_user(client):
    response = client.post("/auth/register/", json={
        "email": "test@example.com",
        "password": "password"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"


def test_login_for_access_token(client):
    client.post("/auth/register/", json={
        "email": "test@example.com",
        "password": "password"
    })

    response = client.post("/token/", data={
        "username": "test@example.com",
        "password": "password"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data