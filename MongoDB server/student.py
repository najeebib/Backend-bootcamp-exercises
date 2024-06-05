from pydantic import BaseModel
class student_model(BaseModel):
    id: str
    first_name: str
    last_name: str
    picture: str

