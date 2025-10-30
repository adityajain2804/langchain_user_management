from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/signup", tags=["Register"])

# Temporary in-memory user database
users_db = []

class User(BaseModel):
    username: str
    password: str

@router.post("/")
def create_user(user: User):
    for u in users_db:
        if u["username"] == user.username:
            return {"error": "Username already exists!"}
    users_db.append(user.dict())
    return {"message": "User created successfully!", "user": user}
