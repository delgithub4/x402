from fastapi import APIRouter
from app.schemas.user import UserCreate

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

users = []

@router.get("/")
def get_users():
    return users

@router.post("/")
def create_user(user: UserCreate):

    new_user = {
        "id": len(users) + 1,
        "name": user.name,
        "email": user.email
    }

    users.append(new_user)

    return {
        "message": "User created successfully",
        "user": new_user
    }
