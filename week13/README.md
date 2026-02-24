# Week 13 – FastAPI with Virtual Environment & User Routes

## 📌 Overview

This project implements a simple User Management API using FastAPI.
It demonstrates:

- Virtual environment setup
- Modular project structure
- FastAPI routing with APIRouter
- Pydantic models
- File-based data persistence (users.txt)
- Health check endpoints

---

## 🏗 Project Structure

week13/
│
├── main.py
├── schema.py
├── users.txt
├── routes/
│   ├── __init__.py
│   └── users.py
└── venv/

---

## ⚙️ Setup Instructions

### 1️⃣ Create Project Folder

```bash
mkdir week13
cd week13
```

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
```

### 3️⃣ Activate Virtual Environment

Mac/Linux:
```bash
source venv/bin/activate
```

Windows:
```bash
venv\Scripts\activate
```

### 4️⃣ Install Dependencies

```bash
pip install fastapi uvicorn
```

---

## 🚀 Running the Application

From inside the `week13` directory:

```bash
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## 🌐 Available Endpoints

### Root Health Check

GET `/`

Response:
```json
{
  "status": "healthy",
  "message": "API is running"
}
```

---

### Detailed Health

GET `/health`

Response:
```json
{
  "status": "ok",
  "service": "User API"
}
```

---

### User Routes

Base path:

```
/users
```

Examples:

- GET `/users`
- POST `/users`
- GET `/users/{id}`
- DELETE `/users/{id}`

---

## 📊 API Documentation (Swagger UI)

Interactive documentation available at:

```
http://127.0.0.1:8000/docs
```

Alternative documentation:

```
http://127.0.0.1:8000/redoc
```

---

## 🧠 Key Concepts Demonstrated

- FastAPI application setup
- APIRouter modular structure
- Pydantic BaseModel for data validation
- JSON file storage
- Exception handling with HTTPException
- Virtual environment isolation

---

## 🗂 Data Persistence

User data is stored in:

```
users.txt
```

Data format: JSON array.

If the file does not exist, it is automatically created.

---

## 🛠 Technologies Used

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic

---

## ✅ Exercise Completion Checklist

- [x] Virtual environment created
- [x] Dependencies installed
- [x] Modular project structure implemented
- [x] User routes created
- [x] Health endpoints added
- [x] Swagger documentation tested
- [x] Application running successfully

---

## 🎯 Conclusion

This lab demonstrates how to build a clean, modular FastAPI backend
with proper environment isolation and structured routing.

The application is fully functional and ready for further extension
(e.g., database integration, authentication, deployment).

---

End of Week 13 Lab.