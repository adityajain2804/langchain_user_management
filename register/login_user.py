from fastapi import APIRouter
from pydantic import BaseModel
from register.create_user import users_db

router = APIRouter(prefix="/login", tags=["Register"])

class Login(BaseModel):
    username: str
    password: str

@router.post("/")
def login_user(login: Login):
    for user in users_db:
        if user["username"] == login.username and user["password"] == login.password:
            return {"message": "Login successful!"}
    return {"error": "Invalid username or password!"}
