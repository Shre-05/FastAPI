from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app=FastAPI()

student={
    "1":{"name":"Shreya","marks":90,"age":22},
    "2":{"name":"Rai","marks":30,"age":22},
    "3":{"name":"Roia","marks":93,"age":20},
    "4":{"name":"sjb","marks":34,"age":23}
}
# get exceptions:
@app.get("/student/{id}")
def get_student(id:str):
    if id not in student:
        raise HTTPException(
            status_code=400,
            detail="student not found"
        )
    return student[id]

# post exception
# when though the datatype has been specified to check if the data given is in the range
# data validation: pydantic->exception check->try and except

class Student(BaseModel):
    id:str
    name:str
    marks:int
    age:int
@app.post("/student/{id}")
def submit_marks(s:Student):
    if s.id not in student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"

        )
    if (s.marks<0 or s.marks>100):
        raise HTTPException(
            status_code=400,
            detail="Enter the valid marks"
        )
    try:
        student[s.id]["marks"]=s.marks
        return{
            "Student id":s.id,
            "Name":student[s.id]["name"],
            "Marks":s.marks
        }
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail="Fault from our side"
        )
    