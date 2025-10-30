from fastapi import FastAPI
from dotenv import load_dotenv
import os

# 🔹 Local module imports
from register import create_user, login_user
from user import add_user, update_user, delete_user, all_users

# Load environment variables
load_dotenv()

app = FastAPI(title=os.getenv("APP_NAME", "FastAPI App"))

# Include routers from both folders
app.include_router(create_user.router)
app.include_router(login_user.router)
app.include_router(add_user.router)
app.include_router(update_user.router)
app.include_router(delete_user.router)
app.include_router(all_users.router)

@app.get("/")
def home():
    return {
        "app_name": os.getenv("APP_NAME"),
        "debug_mode": os.getenv("DEBUG"),
        "admin_user": os.getenv("ADMIN_USER"),
        "message": "Welcome to FastAPI User Management Project!"
    }
