from fastapi import FastAPI
from app.routers import users, auth
from fastapi.responses import JSONResponse
from app.routers import auth, product, users

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(product.router)


@app.get("/")
async def root():
    return {"message": "Server is running"}


@app.get("/health")
async def health_check():
    return JSONResponse(content={"status": "Ok"})
