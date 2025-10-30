from fastapi import APIRouter
from register.create_user import users_db

router = APIRouter(prefix="/users", tags=["User Actions"])

@router.get("/")
def get_all_users():
    return {"total_users": len(users_db), "users": users_db}
