from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI()


class TaskInput(BaseModel):
    title: str
    completed: bool = False


class Task(TaskInput):
    id: int


tasks: list[Task] = []
next_task_id = 1


@app.get("/")
def read_root():
    # TODO: Return a message confirming the API is running.
    pass


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    # TODO: Return all tasks.
    pass


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskInput):
    # TODO: Assign an ID, save the task, and return it.
    pass


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    # TODO: Find and return the task, or raise HTTPException with status 404.
    raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_data: TaskInput):
    # TODO: Update and return the task, or raise HTTPException with status 404.
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    # TODO: Delete the task and return an empty 204 response, or raise HTTPException with status 404.
    raise HTTPException(status_code=404, detail="Task not found")
