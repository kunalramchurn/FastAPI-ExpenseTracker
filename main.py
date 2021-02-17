from fastapi import Depends, FastAPI,status,HTTPException,File,UploadFile
from sqlalchemy.orm import Session
import models,schemas,crud
from uploadfile import parse_csv,convertBytesToString
from database import SessionLocal,engine
from models import Expense
from schemas import ExpenseRequest
from typing import Optional
from pydantic import BaseModel  #use pydantic for data validation

#bind database,models,crud,schemas to main
models.Base.metadata.create_all(bind=engine)

tags_metadata = [
    {
        "name": "Expense Creation",
        "description": "Endpoint to create expenses and store in the database",
    },
    {
        "name": "Retrieve all expenses",
        "description": "Endpoint to retrieve all expenses per items"
       
        },
    
]

#create app session router
app=FastAPI(title='Expense Tracker',version=1.0,description= 'API for tracking expenses',openapi_tags=tags_metadata)

#create database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#define event handlers that need to be executed before the app starts or when the app shuts down, the shutdown event will write a text line application shutdown to a file log.text. 
#((mode=a means append))    
@app.on_event('startup')
async def startup_event():
   print('connnecting')

@app.on_event("shutdown")
async def shutdown_event():
    with open("log.txt", mode="a") as log:
        log.write("Application shutdown")

#create CRUD endpoints
#define root url 
@app.get("/")
def root_url():
    return {'mode':'beta'}

#post/create request 
@app.post("/expenses",tags=['Expense Creation'],status_code=status.HTTP_201_CREATED)
async def create_expense(expense_request: ExpenseRequest,db: Session = Depends(get_db)):
    expense = Expense()
    expense.date = expense_request.date
    expense.description = expense_request.description
    expense.currency = expense_request.currency
    expense.amount= expense_request.amount
    db.add(expense)
    db.commit()
    return {'expense created!!'}

#get request to retrieve expense by Id and designing both path params(expense_id) and query params called q   
@app.get('/expenses/{expense_id}',status_code= status.HTTP_200_OK)
async def get_expense(expense_id:int, q: Optional[str]=None, db: Session = Depends(get_db)):
    if expense_id is None:
        raise HTTPException(status_code=404,detail='Expense not found')
    return db.query(models.Expense).filter(models.Expense.id == expense_id).first()


#returns a dict of all expenses in the databse between 0 - 50
@app.get('/expenses',tags=["Retrieve all expenses"])
async def list_expenses(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return db.query(models.Expense).offset(skip).limit(limit).all()

#fileupload #CONNECT UPLOAD TO DB
@app.post("/fileupload/") 
async def parsecsv(file:UploadFile = File('/Users/kramchurn/Desktop'),db : Session = Depends(get_db)):
    contents = await file.read()
    json_string = convertBytesToString(contents)
    return {'file contents': json_string}
    db.add(json_string)
    db.commit()

