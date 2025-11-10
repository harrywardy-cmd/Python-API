# Flask API Demo

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-API-green?logo=flask)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

A simple **Flask API demo** showcasing **CRUD operations (Create, Read, Update, Delete)** for user management.  
Ideal for learning RESTful API design or creating a base for backend projects.

---

##  Features

 Retrieve all users  
 Retrieve a user by ID  
 Create a new user  
 Update existing user data  
 Delete a user  
 Supports JSON body & query parameters  
 Runs locally with Flask debug mode  

---

##  Endpoints Overview

| Method | Endpoint | Description |
|:-------|:----------|:-------------|
| **GET** | `/users` | Get all users |
| **GET** | `/users/<user_id>` | Get a user by ID |
| **POST** | `/users` | Create a new user |
| **PUT** | `/users/<user_id>` | Update an existing user |
| **DELETE** | `/users/<user_id>` | Delete a user by ID |

---

##  Requirements

- Python **3.8+**
- Flask **(install via pip)**

```bash
pip install flask
```

---

##  How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/flask-api-demo.git
   cd flask-api-demo
   ```

2. Run the app:
   ```bash
   python app.py
   ```

3. Open your browser or API tool (like Postman):
   ```
   http://127.0.0.1:5000
   ```

---

##  Example Requests

###  **GET all users**
```bash
curl http://127.0.0.1:5000/users
```

###  **GET user by ID**
```bash
curl http://127.0.0.1:5000/users/1
```

###  **POST create new user**
```bash
curl -X POST http://127.0.0.1:5000/users      -H "Content-Type: application/json"      -d '{"user_id": "3", "name": "Alice", "email": "alice@example.com"}'
```

###  **PUT update user**
```bash
curl -X PUT http://127.0.0.1:5000/users/3      -H "Content-Type: application/json"      -d '{"email": "alice.new@example.com"}'
```

###  **DELETE user**
```bash
curl -X DELETE http://127.0.0.1:5000/users/3
```

---

##  Example Use Cases

- Beginner-friendly **Flask REST API boilerplate**
- Quick **demo for frontend integration testing**
- Sandbox for **Postman or curl** API practice

---

##  Configuration

By default, Flask runs in **debug mode** for development.  
To disable it (e.g., in production):

```python
app.run(debug=False)
```

---

##  License

This project is licensed under the **MIT License**.  
Feel free to fork, modify, and use it for your own projects.

---

###  Created by Harry Ward(https://github.com/harrywardy-cmd)
