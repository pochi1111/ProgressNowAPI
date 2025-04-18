from fastapi import APIRouter
from starlette.responses import JSONResponse
from DB.controls import UserController

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("/{user_id}")
async def get_user(user_id: str):
    user_controller = UserController()
    user = user_controller.get_user(user_id)
    if user is None:
        return JSONResponse(content={"message": "User not found"}, status_code=404)
    return {
        "id": user.id,
        "provider_id": user.provider_id,
        "email": user.email,
        "name": user.name,
        "created_at": user.created_at,
        "updated_at": user.updated_at
    }