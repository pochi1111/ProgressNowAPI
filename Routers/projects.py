from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import JSONResponse
from DB.controls import ProjectController

class Project(BaseModel):
    admin_id: str
    project_name: str

router = APIRouter(
    prefix="/projects",
    tags=["projects"],
)

@router.get("/{project_id}")
async def get_project(project_id: int):
    project_controller = ProjectController()
    try:
        project = project_controller.get_project_by_id(project_id)
    except Exception as e:
        project_controller.close()
        if str(e)[:3].isdigit():
            return JSONResponse(content={"error_code": str(e)[:3], "message": str(e)}, status_code=int(str(e)[:3]))
        else:
            return JSONResponse(content={"message": "Internal Server Error\n"+str(e)}, status_code=500)
    project_controller.close()
    if project is None:
        return JSONResponse(content={"message": "Project not found"}, status_code=404)
    return {
        "id": project.id,
        "admin_id": project.admin_id,
        "project_name": project.project_name,
        "created_at": project.created_at,
        "updated_at": project.updated_at
    }

@router.post("/")
async def create_project(project: Project):
    project_controller = ProjectController()
    try:
        new_project = project_controller.create_project(admin_id=project.admin_id, project_name=project.project_name)
    except Exception as e:
        project_controller.close()
        if str(e)[:3].isdigit():
            return JSONResponse(content={"error_code": str(e)[:3], "message": str(e)}, status_code=int(str(e)[:3]))
        else:
            return JSONResponse(content={"message": "Internal Server Error\n"+str(e)}, status_code=500)
    project_controller.close()
    if new_project is None:
        return JSONResponse(content={"message": "Error creating project"}, status_code=500)
    return {
        "id": new_project.id,
        "admin_id": new_project.admin_id,
        "project_name": new_project.project_name,
        "created_at": new_project.created_at,
        "updated_at": new_project.updated_at
    }

@router.put("/{project_id}")
async def update_project(project_id: int, project: Project):
    project_controller = ProjectController()
    try:
        updated_project = project_controller.update_project(
            project_id=project_id,
            project_name=project.project_name,
            admin_id=project.admin_id
        )
    except Exception as e:
        project_controller.close()
        if str(e)[:3].isdigit():
            return JSONResponse(content={"error_code": str(e)[:3], "message": str(e)}, status_code=int(str(e)[:3]))
        else:
            return JSONResponse(content={"message": "Internal Server Error\n"+str(e)}, status_code=500)
    project_controller.close()
    if updated_project is None:
        return JSONResponse(content={"message": "Error updating project"}, status_code=500)
    return {
        "id": updated_project.id,
        "admin_id": updated_project.admin_id,
        "project_name": updated_project.project_name,
        "created_at": updated_project.created_at,
        "updated_at": updated_project.updated_at
    }

@router.delete("/{project_id}")
async def delete_project(project_id: int):
    project_controller = ProjectController()
    try:
        result = project_controller.delete_project(project_id)
    except Exception as e:
        project_controller.close()
        if str(e)[:3].isdigit():
            return JSONResponse(content={"error_code": str(e)[:3], "message": str(e)}, status_code=int(str(e)[:3]))
        else:
            return JSONResponse(content={"message": "Internal Server Error\n"+str(e)}, status_code=500)
    project_controller.close()
    if result == 204:
        return JSONResponse(status_code=204)
    elif result == 404:
        return JSONResponse(content={"message": "Project not found"}, status_code=404)
    else:
        return JSONResponse(content={"message": "Error deleting project"}, status_code=500)