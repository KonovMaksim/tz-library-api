def test_borrow_and_return_book(client):
    # Регистрация и авторизация
    client.post("/auth/register/", json={
        "email": "borrowuser@example.com",
        "password": "password"
    })
    login = client.post("/token/", data={
        "username": "borrowuser@example.com",
        "password": "password"
    })
    token = login.json()["access_token"]

    # Создать книгу
    book = client.post("/books/", json={
        "title": "Пример книги",
        "author": "Автор"
    }, headers={"Authorization": f"Bearer {token}"}).json()

    # Создать читателя
    reader = client.post("/readers/", json={
        "name": "Петр Петров",
        "email": "petr@example.com"
    }, headers={"Authorization": f"Bearer {token}"}).json()

    # Выдать книгу
    borrow_response = client.post("/borrow/", json={
        "book_id": book["id"],
        "reader_id": reader["id"]
    }, headers={"Authorization": f"Bearer {token}"})
    assert borrow_response.status_code == 200

    # Вернуть книгу
    return_response = client.post("/borrow/return/", json={
        "book_id": book["id"],
        "reader_id": reader["id"]
    }, headers={"Authorization": f"Bearer {token}"})
    assert return_response.status_code == 200