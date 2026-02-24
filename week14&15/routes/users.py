from fastapi import APIRouter, HTTPException
from schema import User
from user_store import UserStore

router = APIRouter()
store = UserStore("users.db")


@router.get("/")
def get_all_users():
    return store.load()


@router.get("/{user_id}")
def get_user(user_id: int):
    user = store.find_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/")
def create_user(user: User):
    existing = store.find_by_id(user.id)
    if existing:
        raise HTTPException(status_code=400, detail="User ID already exists")

    store.create_user(user.dict())
    return {"message": "User created successfully"}


@router.put("/{user_id}")
def update_user(user_id: int, user: User):
    updated = store.update_user(user_id, user.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User updated successfully"}


@router.delete("/{user_id}")
def delete_user(user_id: int):
    deleted = store.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted successfully"}