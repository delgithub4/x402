from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

users = [
    {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com"
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "email": "jane@example.com"
    }
]

@router.get("/")
def get_users():
    return users

@router.get("/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user

    return {
        "error": "User not found"
      }
