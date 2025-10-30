from fastapi import APIRouter
from pydantic import BaseModel
from register.create_user import users_db

router = APIRouter(prefix="/delete", tags=["User Actions"])

class DeleteUser(BaseModel):
    username: str

@router.delete("/")
def delete_user(data: DeleteUser):
    for user in users_db:
        if user["username"] == data.username:
            users_db.remove(user)
            return {"message": "User deleted successfully!"}
    return {"error": "User not found!"}
