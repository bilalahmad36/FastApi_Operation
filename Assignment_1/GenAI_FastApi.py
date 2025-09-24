from fastapi import FastAPI, HTTPException
from typing import List, Dict
import GenAI_Database
from pydantic import BaseModel

GenAI_Database.init()

app = FastAPI(title = " GenAI ToDo Application")

class TaskCreate(BaseModel):
    title: str


@app.post("/tasks")
def create_task(task : TaskCreate):
    GenAI_Database.add_task(task.title)
    return {"message": "Task added successfully", "title": task.title}


@app.get("/tasks/")
def get_task():
    return GenAI_Database.list_task()


@app.put("/tasks/{ID}")
def complete_task(ID):
    GenAI_Database.mark_completed(ID)
    return {"id": ID, "completed": True} 



@app.delete("/tasks/{ID}")
def remove(ID):
    GenAI_Database.delete_task(ID)
    return {"message": "Task deleted"}    