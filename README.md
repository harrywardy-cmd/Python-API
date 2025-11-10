# 🧩 Flask API Demo

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-API-green?logo=flask)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

A simple **Flask API demo** showcasing **CRUD operations (Create, Read, Update, Delete)** for user management.  
Ideal for learning RESTful API design or creating a base for backend projects.

---

## Features

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

## 🧰 Requirements

- Python **3.8+**
- Flask **(install via pip)**

```bash
pip install flask