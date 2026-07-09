from typing import Optional
from fastapi import FastAPI, Path, Query
from helpers import fail, success
from pydantic import BaseModel

app = FastAPI()
# Run with: python -m uvicorn main:app --reload

students = {
    1: {
        "name": "Asda",
        "age": 21,
        "dob": "26-April-2005",
    }
}

class Student(BaseModel):
    name: str
    age : int
    dob : str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    dob: Optional[str] = None


@app.get("/")
def index():
    return success(students)


@app.get("/student/{student_id}")
def get_student_by_id(
    student_id: int = Path(
        ..., description="The ID of the student you want to view", gt=0
    )
):
    if student_id not in students:
        return fail("Student not found", code=404)
    return success(students[student_id])


@app.get("/student")
def get_student_by_name(name: str = Query(...)):
    for student in students.values():
        if student["name"] == name:
            return success(student)
    return fail("Student name not found", code=404)


# Combining path and query parameters.
@app.get("/combine/{student_id}")
def get_student_by_id_and_name(
    student_id: int,
    name: str = Query(...),
    test: Optional[int] = None,
):
    student = students.get(student_id)
    if student and student["name"] == name:
        return success(student)
    return fail("Student not found", code=404)

# Request body and the post method.
@app.post("/create/{student_id}")
def create_student(
    student_id: int,
    student: Student
):
    if student_id in students:
        return fail("Student exists!", code=400)
    students[student_id] = student.dict()
    return success(students[student_id])

# Request body and the put method.
@app.put("/update/{student_id}")
def update_student(
    student_id: int,
    student: UpdateStudent
):
    if student_id not in students:
        return fail("Student does not exist!", code=404)

    update_data = student.dict(exclude_unset=True)
    students[student_id].update(update_data)
    return success(students[student_id])