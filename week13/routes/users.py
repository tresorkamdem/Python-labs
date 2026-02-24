from fastapi import APIRouter, HTTPException
from schema import User
import json
import os

router = APIRouter()
DATA_FILE = "users.txt"

def read_users():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return []

def write_users(users):
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=2)

@router.get("/")
def get_users():
    return read_users()

@router.post("/")
def create_user(user: User):
    users = read_users()
    users.append(user.dict())
    write_users(users)
    return {"message": "User created successfully"}

@router.get("/{user_id}")
def get_user(user_id: int):
    users = read_users()
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{user_id}")
def delete_user(user_id: int):
    users = read_users()
    updated_users = [u for u in users if u["id"] != user_id]

    if len(users) == len(updated_users):
        raise HTTPException(status_code=404, detail="User not found")

    write_users(updated_users)
    return {"message": "User deleted successfully"}