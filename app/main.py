from fastapi import FastAPI
from app.schemas import Job
from app.database import engine
from app import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
@app.get("/")
def home():
    return{"message":"this is a job application tracker"}

@app.post("/add_job")
async def create_job(job : Job):
    return{"Job":job}