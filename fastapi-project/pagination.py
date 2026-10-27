# returning data in small portions
from fastapi import FastAPI,Query
import json

app=FastAPI()
def get_data():
    with open("student.json","r") as file:
        return json.load(file)

@app.get("/pagination")
def pagination(
    page:int=Query(0,ge=0),
    limit:int=Query(0,ge=0,le=100)
):
    data=get_data()
    students=data["students"]
    skip=(page-1)*limit
    return students[skip:skip+limit]