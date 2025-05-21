def test_create_book(client):
    # Получаем токен
    register_response = client.post("/auth/register/", json={
        "email": "bookuser@example.com",
        "password": "password"
    })
    login_response = client.post("/token/", data={
        "username": "bookuser@example.com",
        "password": "password"
    })
    token = login_response.json()["access_token"]

    # Создание книги
    response = client.post("/books/", json={
        "title": "Война и мир",
        "author": "Лев Толстой"
    }, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Война и мир"


def test_get_books(client):
    response = client.get("/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)