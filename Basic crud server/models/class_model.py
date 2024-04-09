from pydantic import BaseModel
class class_model(BaseModel):
    name: str
    id: int
    teacher: str
    topics: list
