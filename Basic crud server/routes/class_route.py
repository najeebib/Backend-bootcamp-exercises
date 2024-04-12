from fastapi import APIRouter, HTTPException, Depends
from models.class_model import class_model
import utils.db_functions as db_fns
import utils.class_functions as class_fns
import utils.student_functions as student_fns
from modules.school_class import SchoolClass
from modules.student import Student
import utils.auth_functions as auth_fns
from modules.logger import Logger
router = APIRouter()

@router.get('/class/classes')
def get_classes( is_logged = Depends(auth_fns.check_token), log = Depends(Logger.log_request)):
    # check if user logged in
    if is_logged:
        # get all student from the db
        return db_fns.load_db('./data/classes.json')
    else:
        raise HTTPException(401, detail="Only logged users can do this")

@router.post('/class/classes')
def add_class( class_: class_model, is_admin = Depends(auth_fns.check_token_if_admin), log = Depends(Logger.log_request)):
    classes = db_fns.load_db('./data/classes.json')
    # check if admin logged in
    if is_admin:
        # check if a class with this id already exists in the db
        if class_fns.find_class_by_id(classes, class_.id):
            raise HTTPException(status_code=403, detail="Class with this id already exists")
        else:
            # make a new class object  then add it to the db
            new_class = SchoolClass(class_.name, class_.id, class_.teacher, class_.topics)
        
            class_fns.add_class(new_class, classes)
            return {"Class  has been added"}
    else:
        raise HTTPException(401, detail="Only admin users can do this")
    
@router.post('/class/classes/{class_id}/{student_id}')
def add_student_to_class(class_id: int, student_id: int, is_admin = Depends(auth_fns.check_token_if_admin), log = Depends(Logger.log_request)):
    if is_admin:
        students_db = db_fns.load_db('./data/students.json')
        classes_db = db_fns.load_db('./data/classes.json')

        studen_info = student_fns.find_student_by_id(student_id, students_db)
        class_info = student_fns.find_student_by_id(class_id, classes_db)

        class_ = SchoolClass(class_info["name"], class_info["id"], class_info["teacher"], class_info["topics"])
        student = Student(studen_info["name"], studen_info["id"], studen_info["age"], studen_info["classes"])

        class_fns.add_student_to_class(class_, classes_db, student, students_db)
        return {"Class  has been added to student"}
    else:
        raise HTTPException(401, detail="Only admin users can do this")

@router.get("/class/classes/{name}")
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
        raise HTTPException(401, detail="Only admin users can do this")
