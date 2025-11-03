from fastapi import APIRouter
from pydantic import BaseModel
from database import users_collection

router = APIRouter(prefix="/delete", tags=["User Actions"])

class DeleteUser(BaseModel):
    username: str

@router.delete("/")
def delete_user(data: DeleteUser):
    result = users_collection.delete_one({"username": data.username})
    if result.deleted_count > 0:
        return {"message": "User deleted successfully!"}
    return {"error": "User not found!"}
