from fastapi import FastAPI, Request
from mongoAPI import mongo_api
from student import student_model
app = FastAPI()



@app.middleware("http")
async def log_req(request:Request, call_next):
    print(f'got req. to: {request.url}, method: {request.method}')
    response = await call_next(request)
    print(request.body)
    return response

@app.get("/students")
def mongo_read():
    students = mongo_api.read()
    return students


@app.get("/student/{id}")
def mongo_read_one(id: str):
    student = mongo_api.read_one(id)
    return student

@app.post("/student")
def mongo_write(student: student_model):
    response = mongo_api.write(student.model_dump())
    return response

@app.put("/student/{id}")
def mongo_update(id: str, student: student_model):
    response = mongo_api.update(id, student.model_dump())
    return response

@app.delete("/student/{id}")
def mongo_delete_one(id: str):
    student = mongo_api.delete(id)
    return student
