# Bookstore Management System API Documentation

**Authentication**

The API requires Token Authentication. To obtain a token, make a POST request to /api/token/ with your username and password.

Example:

```curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "username=your_username&password=your_password" http://localhost:8000/api/token/```

Write this code in your terminal and replace : username = r4ghuveer, password = bookstore

Include the obtained token in the Authorization header of your requests.

## Endpoints

**1. Add a New Book** 

Endpoint: /api/books/

Method: POST

Headers:

- Authorization: Token <your_token>

Request Body:

json

```
{
  "title": "Book Title",
  "author": "Author Name",
  "isbn": "ISBN Number",
  "price": 29.99,
  "quantity": 50
}
```

Response:

json

```
{
  "id": 1,
  "title": "Book Title",
  "author": "Author Name",
  "isbn": "ISBN Number",
  "price": 29.99,
  "quantity": 50
}
```


**2. Retrieve All Books**

Endpoint: /api/books/

Method: GET

Headers:

- Authorization: Token <your_token>

Response:

json

```
[
  {
    "id": 1,
    "title": "Book Title 1",
    "author": "Author 1",
    "isbn": "ISBN-001",
    "price": 29.99,
    "quantity": 50
  },
  {
    "id": 2,
    "title": "Book Title 2",
    "author": "Author 2",
    "isbn": "ISBN-002",
    "price": 19.99,
    "quantity": 30
  }
  // ... (more books)
]
```

**3. Retrieve a Specific Book by ISBN**

Endpoint: /api/books/\<str:isbn\>/

Method: GET

Headers:

- Authorization: Token <your_token>

Response:

json

```
{
  "id": 1,
  "title": "Book Title",
  "author": "Author Name",
  "isbn": "ISBN Number",
  "price": 29.99,
  "quantity": 50
}
```

**4. Update Book Details**

Endpoint: /api/books/\<int:pk\>/

Method: PUT or PATCH

> Note : Use 'Put' to update the data where you will have to rewrite the entire json and the part you want to edit; Use 'Patch' to update the data where you just have to update the new data.

Headers:

- Authorization: Token <your_token>

Request Body:

json

```
{
  "title": "Updated Title",
  "price": 34.99,
  "quantity": 60
}
```

Response:

json

```
{
  "id": 1,
  "title": "Updated Title",
  "author": "Author Name",
  "isbn": "ISBN Number",
  "price": 34.99,
  "quantity": 60
}
```

**5. Delete a Book**

Endpoint: /api/books/<int:pk>/

Method: DELETE

Headers:

- Authorization: Token <your_token>

Response: No Content
