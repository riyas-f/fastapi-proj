
from app.db.db import db

cursor, conn = db()

def create_teacher(full_name, email):
    try:
        cursor.execute("INSERT INTO TBL_Teachers (FullName, Email) VALUES (%s, %s);", (full_name, email,))
        conn.commit()
    except:
        return 0
    return 1

def get_teacher(teacher_id):
    try:
        cursor.execute("SELECT * FROM TBL_Teachers WHERE TeacherId = %s;", (teacher_id,))
        teacher = cursor.fetchone()
    except:
        return None
    return teacher

def get_All_teacher():
    try:
        cursor.execute(
                    'SELECT * FROM TBL_Teachers')
        teacher = cursor.fetchall()
    except:
        return 0
    return teacher


def update_teacher(teacher_id, full_name, email):
    try:
        cursor.execute("UPDATE TBL_Teachers SET FullName = %s, Email = %s WHERE TeacherId = %s;", (full_name, email, teacher_id,))
        conn.commit()
    except:
        return 0
    return 1

def delete_teacher(teacher_id):
    try:
        cursor.execute("DELETE FROM TBL_Teachers WHERE TeacherId = %s;", (teacher_id,))
        conn.commit()
    except:
        return 0
    return 1

def create_student(full_name, email):
    try:
        cursor.execute("INSERT INTO TBL_Students (FullName, Email) VALUES (%s, %s);", (full_name, email,))
        conn.commit()
    except:
        return 0
    return 1

def get_student(student_id):
    try:
        cursor.execute("SELECT * FROM TBL_Students WHERE StudentId = %s;", (student_id,))
        student = cursor.fetchone()
    except:
        return None
    return student

def get_All_student():
    try:
        cursor.execute(
                    'SELECT * FROM TBL_Students')
        student = cursor.fetchall()
    except:
        return 0
    return student


def update_student(student_id, full_name, email):
    try:
        cursor.execute("UPDATE TBL_Students SET FullName = %s, Email = %s WHERE StudentId = %s;", (full_name, email, student_id,))
        conn.commit()
    except:
        return 0
    return 1

def delete_student(student_id):
    try:
        cursor.execute("DELETE FROM TBL_Students WHERE StudentId = %s;", (student_id,))
        conn.commit()
    except:
        return 0
    return 1

def assign_student_to_teacher(teacher_id, student_id):
    try:
        cursor.execute("INSERT INTO TBL_TeacherStudentAssignments (TeacherId, StudentId) VALUES (%s, %s);", (teacher_id, student_id,))
        conn.commit()
    except:
        return 0
    return 1

def get_All_assign():
    try:
        cursor.execute(
                    'SELECT * FROM TBL_TeacherStudentAssignments')
        assigns = cursor.fetchall()
    except:
        return 0
    return assigns