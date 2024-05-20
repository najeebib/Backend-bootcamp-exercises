from fastapi import FastAPI, Request
from routes import customers_route
import logging


logging.basicConfig(level=logging.INFO, filename="log files/server.log", filemode="w")
app  = FastAPI()

app.include_router(customers_route.router)



@app.middleware("http")
async def log_req(request:Request, call_next):
    print(f'got req. to: {request.url}, method: {request.method}')
    response = await call_next(request)
    return response

@app.get("/")
def root():
    return "hi from fast api"