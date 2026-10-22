from fastapi import FastAPI
from routers import items
from routers import users
from fastapi.responses import JSONResponse

app = FastAPI()

app.include_router(items.router)
app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "Website is running"}


@app.get("/hello")
async def read_hello():
    return JSONResponse({"message": "Hello wannn, nice to meet you!"}, status_code=200)
