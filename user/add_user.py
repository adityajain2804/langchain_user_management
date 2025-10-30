from fastapi import APIRouter
from pydantic import BaseModel
from register.create_user import users_db

router = APIRouter(prefix="/add", tags=["User Actions"])

class User(BaseModel):
    username: str
    password: str

@router.post("/")
def add_user(user: User):
    users_db.append(user.dict())
    return {"message": "User added successfully!", "total_users": len(users_db)}
