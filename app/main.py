from fastapi import FastAPI
from app.routers import items
from app.routers import users
from fastapi.responses import JSONResponse

app = FastAPI()

app.include_router(items.router)
app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "Website is running"}


@app.get("/health")
async def health_check():
    return JSONResponse(content={"status": "Ok"})
