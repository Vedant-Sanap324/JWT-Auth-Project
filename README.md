# 🔐 JWT Authentication System (FastAPI + PostgreSQL)

A complete backend authentication system built using FastAPI with JWT-based authentication and PostgreSQL database.

---

## 🚀 Features

- User Registration
- Secure Password Hashing (bcrypt)
- JWT Token-based Authentication
- Protected Routes (Authorization)
- PostgreSQL Database Integration
- OAuth2 Password Flow (Swagger supported)

---

## 🛠️ Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT (python-jose)
- Passlib (bcrypt)

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|--------|---------|------------|
| POST | /auth/register | Register user |
| POST | /auth/login | Login & get token |
| GET | /auth/profile | Get current user (Protected) |

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/Vedant-Sanap324/JWT-Auth-Project.git
cd JWT-Auth-Project

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload