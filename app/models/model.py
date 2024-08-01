
# model.py
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import List, Optional


def generate_date():

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    return str(dt_string)



class UserSchema(BaseModel):

    UserFullName: str
    UserEmail: EmailStr
    UserPassword: str

class UserLoginSchema(BaseModel):

    LoginEmail: EmailStr
    LoginPassword: str


class TeacherSchema(BaseModel):
    TeacherId: int
    FullName: str
    Email: EmailStr

class StudentSchema(BaseModel):
    StudentId: int
    FullName: str
    Email: EmailStr

class AssignStudentSchema(BaseModel):
    TeacherId: int
    StudentId: int


class DistanceRequestSchema(BaseModel):
    lat1: float
    lon1: float
    lat2: float
    lon2: float
