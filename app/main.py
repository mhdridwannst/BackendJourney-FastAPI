from fastapi import FastAPI
from app.routers import items, users, auth
from fastapi.responses import JSONResponse

app = FastAPI()

app.include_router(items.router)
app.include_router(users.router)
app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message": "Website is running"}


@app.get("/health")
async def health_check():
    return JSONResponse(content={"status": "Ok"})
