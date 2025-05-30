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

@router.get("/email/{email}")
async def get_user(email: str):
    user_controller = UserController()
    try:
        user = user_controller.get_user_by_email(email)
    except Exception as e:
        user_controller.close()
        if str(e)[:3].isdigit():
            return JSONResponse(content={"error_code": str(e)[:3], "message": str(e)}, status_code=int(str(e)[:3]))
        else:
            return JSONResponse(content={"message": "Internal Server Error\n"+str(e)}, status_code=500)
    user_controller.close()
    if user is int:
        return JSONResponse(content={"message": "Error"}, status_code=user)
    return {
        "id": user.id,
        "uid": user.uid,
        "email": user.email,
        "name": user.name,
        "created_at": user.created_at,
        "updated_at": user.updated_at
    }

@router.get("/uid/{uid}")
async def get_user_by_uid(uid: str):
    user_controller = UserController()
    try:
        user = user_controller.get_user_by_uid(uid)
    except Exception as e:
        user_controller.close()
        if str(e)[:3].isdigit():
            return JSONResponse(content={"error_code": str(e)[:3], "message": str(e)}, status_code=int(str(e)[:3]))
        else:
            return JSONResponse(content={"message": "Internal Server Error\n"+str(e)}, status_code=500)
    user_controller.close()
    if user is int:
        return JSONResponse(content={"message": "Error"}, status_code=user)
    return {
        "id": user.id,
        "uid": user.uid,
        "email": user.email,
        "name": user.name,
        "created_at": user.created_at,
        "updated_at": user.updated_at
    }

@router.get("/id/{user_id}")
async def get_user_by_id(user_id: int):
    user_controller = UserController()
    try:
        user = user_controller.get_user_by_id(user_id)
    except Exception as e:
        user_controller.close()
        if str(e)[:3].isdigit():
            return JSONResponse(content={"error_code": str(e)[:3], "message": str(e)}, status_code=int(str(e)[:3]))
        else:
            return JSONResponse(content={"message": "Internal Server Error\n"+str(e)}, status_code=500)
    user_controller.close()
    if user is int:
        return JSONResponse(content={"message": "Error"}, status_code=user)
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
    try:
        result = user_controller.delete_user(uid)
    except Exception as e:
        user_controller.close()
        if str(e)[:3].isdigit():
            return JSONResponse(content={"error_code": str(e)[:3], "message": str(e)}, status_code=int(str(e)[:3]))
        else:
            return JSONResponse(content={"message": "Internal Server Error\n"+str(e)}, status_code=500)
    user_controller.close()
    return JSONResponse(content={"message": "User deleted successfully"}, status_code=result) if result == 204 else JSONResponse(content={"message": "User not found"}, status_code=result)