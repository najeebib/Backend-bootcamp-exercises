from fastapi import FastAPI, Request, Depends
from routes import students_route, auth_route
import logging
from modules.logger import Logger


logging.basicConfig(level=logging.INFO, filename="log files/server.log", filemode="w")
app  = FastAPI(dependencies=[Depends(Logger.log_request)])

app.include_router(students_route.router)
app.include_router(auth_route.router)


@app.middleware("http")
async def log_req(request:Request, call_next):
    print(f'got req. to: {request.url}, method: {request.method}')
    response = await call_next(request)
    return response

@app.get("/")
def root():
    return "hi from fast api"