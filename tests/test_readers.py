def test_create_reader(client):
    # Логин
    client.post("/auth/register/", json={
        "email": "readeruser@example.com",
        "password": "password"
    })
    login = client.post("/token/", data={
        "username": "readeruser@example.com",
        "password": "password"
    })
    token = login.json()["access_token"]

    # Создание читателя
    response = client.post("/readers/", json={
        "name": "Иван Иванов",
        "email": "ivan@example.com"
    }, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "ivan@example.com"


def test_get_readers(client):
    response = client.get("/readers/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)