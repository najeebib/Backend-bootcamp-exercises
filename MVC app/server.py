from fastapi import FastAPI, Request
from routes import auth_route
from routes import products_route

import logging
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory="templates")
app = FastAPI()

app.include_router(auth_route.router)
app.include_router(products_route.router)


app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/sign_in')
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

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

@app.get("/log_out")
def logout(request: Request):
    return templates.TemplateResponse("logout.html", {"request": request})