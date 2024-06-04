from pydantic import BaseModel
class student_model(BaseModel):
    first_name: str
    last_name: str
    picture: str

