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
    user_controller.close()
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

@router.update("/{user_id}")
async def update_user(user_id: str, email: str = None, name: str = None):
    user_controller = UserController()
    try:
        user = user_controller.update_user(user_id, email, name)
    except Exception as e:
        # TODO: エラーメッセージを投げた時にそれが本当にeに代入されているかどうかを確認する
        user_controller.close()
        if str(e)[:3].isdigit():
            return JSONResponse(content={"error_code": str(e)[:3], "message": str(e)}, status_code=int(str(e)[:3]))
        else:
            return JSONResponse(content={"message": "Internal Server Error\n"+str(e)}, status_code=500)
    user_controller.close()
    return {
        "id": user.id,
        "provider_id": user.provider_id,
        "email": user.email,
        "name": user.name,
        "created_at": user.created_at,
        "updated_at": user.updated_at
    }

@router.post("/")
