from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import JSONResponse
from DB.controls import TaskController

class Task(BaseModel):
    project_id: int
    task_name: str
    description: str = None

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)

@router.get("/{task_id}")
async def get_task(task_id: int):
    task_controller = TaskController()
    try:
        task = task_controller.get_task_by_id(task_id)
    except Exception as e:
        task_controller.close()
        if str(e)[:3].isdigit():
            return JSONResponse(content={"error_code": str(e)[:3], "message": str(e)}, status_code=int(str(e)[:3]))
        else:
            return JSONResponse(content={"message": "Internal Server Error\n"+str(e)}, status_code=500)
    task_controller.close()
    if task is None:
        return JSONResponse(content={"message": "Task not found"}, status_code=404)
    return {
        "id": task.id,
        "project_id": task.project_id,
        "task_name": task.task_name,
        "description": task.description,
        "created_at": task.created_at,
        "updated_at": task.updated_at
    }

@router.get("/project/{project_id}")
async def get_tasks_by_project(project_id: int):
    task_controller = TaskController()
    try:
        tasks = task_controller.get_tasks_by_project_id(project_id)
    except Exception as e:
        task_controller.close()
        if str(e)[:3].isdigit():
            return JSONResponse(content={"error_code": str(e)[:3], "message": str(e)}, status_code=int(str(e)[:3]))
        else:
            return JSONResponse(content={"message": "Internal Server Error\n"+str(e)}, status_code=500)
    task_controller.close()
    if not tasks:
        return JSONResponse(content={"message": "No tasks found for this project"}, status_code=404)
    return [{"id": task.id, "project_id": task.project_id, "task_name": task.task_name, "description": task.description, "created_at": task.created_at, "updated_at": task.updated_at} for task in tasks]

@router.post("/")
async def create_task(task: Task):
    task_controller = TaskController()
    try:
        new_task = task_controller.create_task(project_id=task.project_id, task_name=task.task_name, description=task.description)
    except Exception as e:
        task_controller.close()
        if str(e)[:3].isdigit():
            return JSONResponse(content={"error_code": str(e)[:3], "message": str(e)}, status_code=int(str(e)[:3]))
        else:
            return JSONResponse(content={"message": "Internal Server Error\n"+str(e)}, status_code=500)
    task_controller.close()
    if new_task is None:
        return JSONResponse(content={"message": "Error creating task"}, status_code=500)
    return {
        "id": new_task.id,
        "project_id": new_task.project_id,
        "task_name": new_task.task_name,
        "description": new_task.description,
        "created_at": new_task.created_at,
        "updated_at": new_task.updated_at
    }

@router.put("/{task_id}")
async def update_task(task_id: int, task: Task):
    task_controller = TaskController()
    try:
        updated_task = task_controller.update_task(
            task_id=task_id,
            project_id=task.project_id,
            task_name=task.task_name,
            description=task.description
        )
    except Exception as e:
        task_controller.close()
        if str(e)[:3].isdigit():
            return JSONResponse(content={"error_code": str(e)[:3], "message": str(e)}, status_code=int(str(e)[:3]))
        else:
            return JSONResponse(content={"message": "Internal Server Error\n"+str(e)}, status_code=500)
    task_controller.close()
    if updated_task is None:
        return JSONResponse(content={"message": "Error updating task"}, status_code=500)
    return {
        "id": updated_task.id,
        "project_id": updated_task.project_id,
        "task_name": updated_task.task_name,
        "description": updated_task.description,
        "created_at": updated_task.created_at,
        "updated_at": updated_task.updated_at
    }

@router.delete("/{task_id}")
async def delete_task(task_id: int):
    task_controller = TaskController()
    try:
        success = task_controller.delete_task(task_id)
    except Exception as e:
        task_controller.close()
        if str(e)[:3].isdigit():
            return JSONResponse(content={"error_code": str(e)[:3], "message": str(e)}, status_code=int(str(e)[:3]))
        else:
            return JSONResponse(content={"message": "Internal Server Error\n"+str(e)}, status_code=500)
    task_controller.close()
    if not success:
        return JSONResponse(content={"message": "Error deleting task"}, status_code=500)
    return JSONResponse(content={"message": "Task deleted successfully"}, status_code=200)