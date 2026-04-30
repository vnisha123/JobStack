from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.schemas import JobCreate, JobOut
from app.database import engine,db_dep
from app.routers.utils import get_current_user
from app import models

router =APIRouter()

@router.post("/jobs/", response_model=JobOut)
async def create_job(
    job: JobCreate, 
    db: db_dep, 
    current_user: models.User = Depends(get_current_user) 
):

    job_data = job.model_dump()

    new_job = models.Job(**job_data, user_id=current_user.id)

    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job