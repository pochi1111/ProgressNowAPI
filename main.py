from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import Routers.users as UsersRouter

app = FastAPI()

app.include_router(UsersRouter.router)

@app.get("/")
async def root():
    return {"status": "Success!"}

@app.exception_handler(404)
def not_found(req: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse(content={"NotFound": str(req.url)}, status_code=404)