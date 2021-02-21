# FastAPI ExpenseTracker

The basis of this app, is to allow a user to create, retrieve,delete and update an expense or multiple expenses. It also contains an endpoint to upload a csv file to record expenses.

Breakdown of this project: 

1. Authentication method: Basic Authentication + OAUTH2 scheme flow using Tortoise ORM(Object Relational Mapping) 
2. Dependency injections, pydantic models and schemas
3. CRUD Endpoints 
4. Deployment through ASGI server using the Uvicorn package
5. Testing endpoints using postman
