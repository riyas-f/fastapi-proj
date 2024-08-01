
# routes.py
from fastapi import APIRouter, Depends, HTTPException
from app.models.model import DistanceRequestSchema, UserSchema, UserLoginSchema
from app.db.user import *
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT
from fastapi.responses import JSONResponse

from app.models.model import TeacherSchema, StudentSchema, AssignStudentSchema
from app.db.school import *
from app.utils import calculate_distance



routes = APIRouter()
router = APIRouter()

@routes.get("/", tags=["hello"])
def hello():
    
    return JSONResponse(content="Hello World", status_code=200)


@routes.post("/user/signup", tags=["users"])
def create_user(user: UserSchema):
    
    flag = createUser(user.UserFullName, user.UserEmail, user.UserPassword)


    if flag==0:
        return JSONResponse(content="Error!", status_code=500)

    else:

        return JSONResponse(content="Add user successful", status_code=201)

@routes.post("/user/login", tags=["users"])
def user_login(user: UserLoginSchema):

    if checkUser(user.LoginEmail, user.LoginPassword):
        return signJWT(user.LoginEmail)
    return JSONResponse(content="Wrong login details!", status_code=500)



@router.post("/teacher/", tags=["teachers"])
def create_teacher_endpoint(teacher: TeacherSchema):
    flag = create_teacher(teacher.FullName, teacher.Email)
    if flag == 0:
        raise HTTPException(status_code=500, detail="Error creating teacher")
    return {"message": "Teacher created successfully"}

@router.get("/teacher/{teacher_id}", tags=["teachers"])
def get_teacher_endpoint(teacher_id: int):
    teacher = get_teacher(teacher_id)
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher


@router.get("/all/teachers/", tags=["teachers"])
def get_all_teachers():
    teachers = get_All_teacher()
    if teachers==0:
        return JSONResponse(content="Error", status_code=500)
    else:
        return JSONResponse(content=teachers, status_code=200)


@router.put("/teacher/", tags=["teachers"])
def update_teacher_endpoint(teacher: TeacherSchema):
    flag = update_teacher(teacher.TeacherId, teacher.FullName, teacher.Email)
    if flag == 0:
        raise HTTPException(status_code=500, detail="Error updating teacher")
    return {"message": "Teacher updated successfully"}

@router.delete("/teacher/{teacher_id}", tags=["teachers"])
def delete_teacher_endpoint(teacher_id: int):
    flag = delete_teacher(teacher_id)
    if flag == 0:
        raise HTTPException(status_code=500, detail="Error deleting teacher")
    return {"message": "Teacher deleted successfully"}

@router.post("/student/", tags=["students"])
def create_student_endpoint(student: StudentSchema):
    flag = create_student(student.FullName, student.Email)
    if flag == 0:
        raise HTTPException(status_code=500, detail="Error creating student")
    return {"message": "Student created successfully"}

@router.get("/student/{student_id}", tags=["students"])
def get_student_endpoint(student_id: int):
    student = get_student(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.get("/all/students/", tags=["students"])
def get_all_students():
    student = get_All_student()
    if student==0:
        return JSONResponse(content="Error", status_code=500)
    else:
        return JSONResponse(content=student, status_code=200)


@router.put("/student/", tags=["students"])
def update_student_endpoint(student: StudentSchema):
    flag = update_student(student.StudentId, student.FullName, student.Email)
    if flag == 0:
        raise HTTPException(status_code=500, detail="Error updating student")
    return {"message": "Student updated successfully"}

@router.delete("/student/{student_id}", tags=["students"])
def delete_student_endpoint(student_id: int):
    flag = delete_student(student_id)
    if flag == 0:
        raise HTTPException(status_code=500, detail="Error deleting student")
    return {"message": "Student deleted successfully"}

@router.post("/assign-student/", tags=["assignments"])
def assign_student_to_teacher_endpoint(assign: AssignStudentSchema):
    flag = assign_student_to_teacher(assign.TeacherId, assign.StudentId)
    if flag == 0:
        raise HTTPException(status_code=500, detail="Error assigning student to teacher")
    return {"message": "Student assigned to teacher successfully"}

@router.get("/all/assigns/", tags=["assignments"])
def get_all_assignments():
    assigns = get_All_assign()
    if assigns==0:
        return JSONResponse(content="Error", status_code=500)
    else:
        return JSONResponse(content=assigns, status_code=200)
    

@routes.post("/calculate-distance/", tags=["distance"])
def calculate_distance_endpoint(request: DistanceRequestSchema):
    try:
        distance = calculate_distance(
            request.lat1, request.lon1, request.lat2, request.lon2
        )
        return {"distance": distance}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))