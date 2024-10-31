
from fastapi import FastAPI , params , Depends , Header 
import uvicorn 
from pydantic import BaseModel

class StudentTy (BaseModel): # type: ignore
    name : str
    rollno : str | int
    age : str | int 
    





Students  = [{
    "Name":"Badar",
    "Rollno" : "46",
    "Age" : "16"
},{
    "Name":"Usman",
    "Rollno": "1",
    "Age": "21"
}]
app = FastAPI()


@app.get("/")
def hi():
    return{"Hello":"World"}


@app.get("/greet/{who}")
def greet(who):
    return {"Asslam-u-Alaikum" : who}

@app.get("/response")
def response(who):
    return "Wa-Alaikum-aslam" , who

@app.get("/Students")
def student():
    return Students 

@app.post("/addStudents")
def addStudents(name:str , rollno:str  , age:str):
     global Students
     Students.append({   "Name":name,"Rollno":rollno,"Age":age        })
     return "Successfull"

@app.delete("/Delete Student")
def delete():
    if Students:
        last_student = Students.pop()  # Removes the last student from the list
        return {"message": "Student deleted successfully", "deleted_student": last_student}
    else:
        return {"message": "No students to delete"}




def start():
    uvicorn.run("hello.main:app", host="127.0.0.1", port=8080, reload=True)