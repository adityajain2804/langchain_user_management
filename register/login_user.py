from fastapi import APIRouter
from pydantic import BaseModel
from database import users_collection

router = APIRouter(prefix="/login", tags=["Register"])

class Login(BaseModel):
    username: str
    password: str

@router.post("/")
def login_user(login: Login):
    user = users_collection.find_one({
        "username": login.username,
        "password": login.password
    })
    if user:
        return {"message": "Login successful!"}
    return {"error": "Invalid username or password!"}
