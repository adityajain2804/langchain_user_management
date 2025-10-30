from fastapi import APIRouter
from pydantic import BaseModel
from register.create_user import users_db

router = APIRouter(prefix="/update", tags=["User Actions"])

class UpdateUser(BaseModel):
    username: str
    new_password: str

@router.put("/")
def update_user(data: UpdateUser):
    for user in users_db:
        if user["username"] == data.username:
            user["password"] = data.new_password
            return {"message": "Password updated successfully!"}
    return {"error": "User not found!"}
