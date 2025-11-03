from fastapi import APIRouter
from pydantic import BaseModel
from database import users_collection

router = APIRouter(prefix="/add", tags=["User Actions"])

class User(BaseModel):
    username: str
    password: str

@router.post("/")
def add_user(user: User):
    if users_collection.find_one({"username": user.username}):
        return {"error": "User already exists!"}
    
    users_collection.insert_one(user.dict())
    total = users_collection.count_documents({})
    return {"message": "User added successfully!", "total_users": total}
