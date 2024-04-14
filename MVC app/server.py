from fastapi import FastAPI, Request
from routes import auth_route
import logging

app = FastAPI()

app.include_router(auth_route.router)

@app.middleware("http")
async def log_req(request:Request, call_next):
    print(f'got req. to: {request.url}, method: {request.method}')
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "*"

    return response

@app.get("/")
def root():
    return "hi from fast api"