from fastapi import APIRouter
from database import users_collection

router = APIRouter(prefix="/users", tags=["User Actions"])

@router.get("/")
def get_all_users():
    users = list(users_collection.find({}, {"_id": 0}))
    total = len(users)
    return {"total_users": total, "users": users}
