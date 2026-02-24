# WEEK 14 & 15 LAB EXERCISE
# From JSON UserStore to SQLite Database (FastAPI)

This project continues the previous FastAPI User Management API and upgrades
its persistence layer from a JSON file-based UserStore to a SQLite database-backed UserStore.

The goal is to move from procedural file handling to a clean object-oriented
data access layer and then upgrade it to a relational database.

------------------------------------------------------------
PROJECT OVERVIEW
------------------------------------------------------------

We build a production-style FastAPI application with:

- FastAPI for REST API
- Pydantic models for validation
- Object-Oriented UserStore class
- SQLite database for persistence
- Full CRUD operations (Create, Read, Update, Delete)

Architecture:

week_project/
│
├── main.py
├── schema.py
├── user_store.py
├── routes/
│   ├── __init__.py
│   └── users.py
├── users.db
└── venv/

------------------------------------------------------------
LAB OBJECTIVES
------------------------------------------------------------

WEEK 14 (OOP Refactor)
- Replace procedural file handling with UserStore class
- Implement load(), save(), find_by_id()
- Refactor endpoints to use store methods
- Add update_user() and delete_user()

WEEK 15 (Database Upgrade)
- Replace JSON storage with SQLite
- Implement init_db()
- Use SQL INSERT / SELECT / UPDATE / DELETE
- Refactor endpoints to use SQLite-backed store
- Test full CRUD with database persistence

------------------------------------------------------------
PART 1 — USERSTORE (SQLITE VERSION)
------------------------------------------------------------

The UserStore class is responsible for:

- Creating the database if it does not exist
- Creating the users table
- Loading users
- Finding users by ID
- Creating new users
- Updating users
- Deleting users

Database schema:

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER
);

------------------------------------------------------------
PART 2 — FASTAPI ENDPOINTS
------------------------------------------------------------

Available API Endpoints:

GET     /                -> Health check
GET     /health          -> Detailed health check

GET     /users           -> Get all users
GET     /users/{id}      -> Get user by ID
POST    /users           -> Create user
PUT     /users/{id}      -> Update user
DELETE  /users/{id}      -> Delete user

------------------------------------------------------------
HOW TO RUN THE PROJECT
------------------------------------------------------------

1. Activate virtual environment:

   source venv/bin/activate

2. Install dependencies:

   pip install fastapi uvicorn

3. Start server:

   uvicorn main:app --reload

4. Open browser:

   http://127.0.0.1:8000/docs

------------------------------------------------------------
TESTING CHECKLIST
------------------------------------------------------------

- GET /users returns empty list initially
- POST /users creates new user
- Data persists in users.db
- GET /users/{id} works
- PUT updates user
- DELETE removes user
- Restart server and verify data remains

------------------------------------------------------------
WHAT WE LEARNED
------------------------------------------------------------

- Clean architecture with separation of concerns
- Object-Oriented persistence layer
- SQL database integration
- CRUD with FastAPI
- Production-style backend structure
- Proper database initialization
- Error handling using HTTPException



------------------------------------------------------------
END OF LAB
------------------------------------------------------------