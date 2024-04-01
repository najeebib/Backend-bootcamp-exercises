from fastapi import APIRouter, HTTPException, Request, status
import utils.db_functions as db_fns
from models.student_model import student_model
from modules.student import Student
import utils.auth_functions as auth_fns
router = APIRouter()


@router.get('/school/students')
def get_students(request: Request):
    # check if user logged in
    if auth_fns.check_token(request):
        # get all student from the db
        return db_fns.load_db('./data/students.json')
    else:
        raise HTTPException(400, "no token")

@router.get('/school/students/{id}')
def get_student(id: int, request: Request):
    # check if user logged in
    if auth_fns.check_token(request):
        students = db_fns.load_db('./data/students.json')
        for _, student_info in students.items():
            if student_info["id"] == id:
                return student_info
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No student with this id exists")
    else:
        raise HTTPException(400, "no token")


@router.post('/school/students')
def add_student(student: student_model, request: Request):
    # check if admin logged in
    if auth_fns.check_token_if_admin(request):
        # check if a student with this id allready exists in the db
        students = db_fns.load_db('./data/students.json')
        for _, student_info in students.items():
            if student_info["id"] == id:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Student with this id allready exists")
        
            # make a new student object  then add it to the db
            new_student = Student(student.name, student.id, student.age, student.classes)
            db_fns.add_student(new_student)
            return {"Stduent  has been added"}
    else:
        raise HTTPException(400, "no token")

@router.get("/school/class/{name}")
def get_class(name: str, request: Request):
    # check if admin logged in
    if auth_fns.check_token_if_admin(request):
        students = db_fns.load_db('./data/students.json')
        students_in_class = []
        # for each student check if they have the class in their classes list
        for _, student_info in students.items():
            if name in student_info["classes"]:
                # add the student to list of students in this class
                students_in_class.append(student_info)
        return students_in_class
    else:
        raise HTTPException(400, "no token")