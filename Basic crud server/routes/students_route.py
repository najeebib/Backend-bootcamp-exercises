from fastapi import APIRouter, HTTPException, Depends
import utils.db_functions as db_fns
import utils.student_functions as student_fns
from models.student_model import student_model
from modules.student import Student
import utils.auth_functions as auth_fns
from modules.logger import Logger
router = APIRouter()


@router.get('/school/students')
def get_students( is_logged = Depends(auth_fns.check_token), log = Depends(Logger.log_request)):
    # check if user logged in
    if is_logged:
        # get all student from the db
        return db_fns.load_db('./data/students.json')
    else:
        raise HTTPException(400, detail="no token")

@router.get('/school/students/{id}')
def get_student( id: int, is_logged = Depends(auth_fns.check_token ), log = Depends(Logger.log_request)):
    # check if user logged in
    if is_logged:
        students = db_fns.load_db('./data/students.json')
        student_info = student_fns.find_student_by_id(id, students)
        if student_info:
            return student_info
        else:
            raise HTTPException(status_code=404, detail="No student with this id exists")        
    else:
        raise HTTPException(400, detail="no token")
@router.post('/school/students')
def add_student( student: student_model, is_admin = Depends(auth_fns.check_token_if_admin), log = Depends(Logger.log_request)):
    students = db_fns.load_db('./data/students.json')
    # check if admin logged in
    if is_admin:
        # check if a student with this id allready exists in the db
        if student_fns.find_student_by_id(student.id, students):
                raise HTTPException(status_code=400, detail="Student with this id allready exists")
        
        # make a new student object  then add it to the db
        new_student = Student(student.name, student.id, student.age, student.classes)
        
        student_fns.add_student(new_student, students)
        return {"Stduent  has been added"}
    else:
        raise HTTPException(400, detail="no token")

@router.put('/school/students/{id}')
def edit_student( id:int, student: student_model, is_admin = Depends(auth_fns.check_token_if_admin), log = Depends(Logger.log_request)):
    students = db_fns.load_db('./data/students.json')
    # check if admin logged in
    if is_admin:
        # check if a student with this id allready exists in the db
        student_info = student_fns.find_student_by_id(id, students)
        if student_info:
            # update the suer info
            student_fns.update_student(id, student, students)
            return {"user was updated"}
        raise HTTPException(status_code=404, detail="No student with this id exists") 
    else:
        raise HTTPException(400, detail="no token")
@router.delete('/school/students/{id}')
def delete_student( id: int, is_admin = Depends(auth_fns.check_token_if_admin), log = Depends(Logger.log_request)):
    students = db_fns.load_db('./data/students.json')
    # check if admin logged in
    if is_admin:
        # check if a student with this id allready exists in the db
        student_info = student_fns.find_student_by_id(id, students)
        if student_info:
            # delete user from db
            student_fns.delete_student(student_info["name"], students)
            return {"user was deleted"}
        raise HTTPException(status_code=404, detail="No student with this id exists") 
    else:
        raise HTTPException(400, detail="no token")
@router.delete('/school/students')
def delete_all_students( is_admin = Depends(auth_fns.check_token_if_admin), log = Depends(Logger.log_request)):
    students = db_fns.load_db('./data/students.json')
    # check if admin logged in
    if is_admin:
        student_fns.delete_all_students(students)
    else:
        raise HTTPException(400, detail="no token")
@router.get("/school/class/{name}")
def get_class( name: str, is_admin = Depends(auth_fns.check_token_if_admin), log = Depends(Logger.log_request)):
    # check if admin logged in
    if is_admin:
        students = db_fns.load_db('./data/students.json')
        students_in_class = []
        # for each student check if they have the class in their classes list
        for _, student_info in students.items():
            if name in student_info["classes"]:
                # add the student to list of students in this class
                students_in_class.append(student_info)
        return students_in_class
    else:
        raise HTTPException(400, detail="no token")