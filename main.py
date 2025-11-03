from fastapi import FastAPI
from dotenv import load_dotenv
import os

from register import create_user, login_user
from user import add_user, update_user, delete_user, all_users

load_dotenv()

app = FastAPI(title=os.getenv("APP_NAME", "FastAPI MongoDB App"))

# Include all routers
app.include_router(create_user.router)
app.include_router(login_user.router)
app.include_router(add_user.router)
app.include_router(update_user.router)
app.include_router(delete_user.router)
app.include_router(all_users.router)

@app.get("/")
def home():
    return {
        "app_name": os.getenv("APP_NAME", "FastAPI App"),
        "message": "Welcome to FastAPI User Management with MongoDB!"
    }
