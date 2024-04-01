from pydantic import BaseModel
class student_model(BaseModel):
    name: str
    id: int
    age: int
    classes: list
