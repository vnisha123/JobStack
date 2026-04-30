from fastapi import FastAPI
from app.routers import auth, users, jobs

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(jobs.router)

@app.get("/")
def home():
    return{"message":"This is a job application tracker"}


