from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import JSONResponse
from DB.controls import UserController

class User(BaseModel):
    uid : str
    email : str
    name : str

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("/{identifier}")
async def get_user(identifier: str):
    user_controller = UserController()
    if "@" in identifier:
        user = user_controller.get_user(identifier)
    else:
        user = user_controller.get_user_by_uid(identifier)
    user_controller.close()
    if user is None:
        return JSONResponse(content={"message": "User not found"}, status_code=404)
    return {
        "id": user.id,
        "uid": user.uid,
        "email": user.email,
        "name": user.name,
        "created_at": user.created_at,
        "updated_at": user.updated_at
    }

@router.post("/")
async def create_user(user: User):
    user_controller = UserController()
    uid = user.uid
    email = user.email
    name = user.name
    try:
        user = user_controller.create_user(uid, email, name)
    except Exception as e:
        user_controller.close()
        if str(e)[:3].isdigit():
            return JSONResponse(content={"error_code": str(e)[:3], "message": str(e)}, status_code=int(str(e)[:3]))
        else:
            return JSONResponse(content={"message": "Internal Server Error\n"+str(e)}, status_code=500)
    user_controller.close()

@router.delete("/{uid}")
async def delete_user(uid: str):
    user_controller = UserController()
    result = user_controller.delete_user(uid)
    user_controller.close()
    if result:
        return JSONResponse(content={"message": "User deleted successfully"}, status_code=200)
    else:
        return JSONResponse(content={"message": "User not found"}, status_code=404)