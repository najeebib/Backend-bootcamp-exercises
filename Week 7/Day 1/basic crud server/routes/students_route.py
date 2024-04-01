from fastapi import APIRouter, HTTPException, Request, status
import utils.data_handler as data_handler
from models.student_model import student_model
from modules.student import Student
router = APIRouter()


@router.get('/students')
def get_stidents():
    # get all student from the db
    return data_handler.get_students()

@router.get('/students/{id}')
def get_student(id: int):
    students = data_handler.get_students()
    for student in students:
        # check if the stydents exists
        if student["id"] == id:
            return student
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No student with this id exists")


@router.post('/students')
def add_student(student: student_model):
    # check if a student with this id allready exists in the db
    students = data_handler.get_students()
    for std in students:
        # check if the stydents exists
        if std["id"] == student.id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Student with this id allready exists")
    # make a new student object  then add it to the db
    new_student = Student(student.name, student.id, student.age, student.classes)
    data_handler.add_student(new_student)
    return {"Stduent  has been added"}

@router.get("/class/{name}")
def get_class(name: str):
    students = data_handler.get_students()
    students_in_class = []
    # for each student check if they have the class in their classes list
    for student in students:
        if name in student["classes"]:
            # add the student to list of students in this class
            students_in_class.append(student)
    return students_in_class