from fastapi import FastAPI,HTTPException
import json

app=FastAPI()

def get_data(): #helper function:which maybe needed again in the code
    with open("student.json","r") as file:
        return json.load(file)
@app.get("/Student_info")    
def print_Student_data():
    return get_data()

@app.get("/Student_info/{student_id}")
def get_id(student_id:str):
    data=get_data()
    for student in data["students"]:
        if student["student_id"]==student_id:
            return student
    raise HTTPException(
        status_code=404,
        detail="Not found"
    )