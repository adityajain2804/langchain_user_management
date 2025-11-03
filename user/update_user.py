from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from bson import ObjectId
from database import users_collection

router = APIRouter(prefix="/update", tags=["User Actions"])

class UpdateUser(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None

@router.put("/{user_id}")
def update_user(user_id: str, data: UpdateUser):
    update_data = {k: v for k, v in data.dict().items() if v is not None}

    if not update_data:
        return {"error": "No fields provided for update."}

    result = users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": update_data}
    )

    if result.matched_count == 0:
        return {"error": "User not found!"}

    if result.modified_count == 0:
        return {"message": "No changes made."}

    return {"message": "User updated successfully!"}
