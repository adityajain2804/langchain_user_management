from fastapi import APIRouter
from pydantic import BaseModel
from database import users_collection

router = APIRouter(prefix="/signup", tags=["Register"])

class User(BaseModel):
    username: str
    password: str

@router.post("/")
def create_user(user: User):
    existing_user = users_collection.find_one({"username": user.username})
    if existing_user:
        return {"error": "Username already exists!"}
    
    users_collection.insert_one(user.dict())
    return {"message": "User created successfully!", "user": user.dict()}
