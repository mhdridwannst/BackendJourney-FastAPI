from fastapi import FastAPI
from routers import items
from routers import users

app = FastAPI()

app.include_router(items.router)
app.include_router(users.router)


@app.get("")
async def root():
    return {"message": "Website is running"}
