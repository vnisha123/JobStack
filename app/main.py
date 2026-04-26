from fastapi import FastAPI
from app.schemas import Job
app = FastAPI()

@app.get("/")
def home():
    return{"message":"this is a job application tracker"}

@app.post("/add_job")
async def create_job(job : Job):
    return{"Job":job}