from fastapi import FastAPI
import model.modelReq as modelReq
import controller.toDoController as im_toDoController

app = FastAPI()
toDoController = im_toDoController.ToDoController()

@app.get("/echo")
def echo():
    return toDoController.read_root()

@app.get("/toDoList")
async def toDoList():
    return toDoController.read_toDoList()

@app.post("/addToDo")
async def addToDo(req:modelReq.DataReq):
    return toDoController.read_insertToDo(req)

@app.post("/editToDo")
async def editToDo(req:modelReq.DataReq):
    return toDoController.read_editToDo(req)

@app.post("/deleteToDo")
async def deleteToDo(req:modelReq.DataReq):
    return toDoController.read_deleteToDo(req)