from fastapi import FastAPI
from app.routers import auth, users, jobs

app = FastAPI(title="Job Tracker API",
    description="A backend for managing job applications with JWT auth",
    version="1.0.0")

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(jobs.router)

@app.get("/")
def home():
    return{"message":"This is a job application tracker"}


