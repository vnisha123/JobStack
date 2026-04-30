from pydantic import BaseModel, Field, ConfigDict, EmailStr
from enum import Enum
from datetime import datetime

class JobStatus(str,Enum):
    INTERESTED = "Interested"
    APPLIED = "Applied"
    INTERVIEWING = "Interviewing"
    OFFER = "Offer"
    REJECTED ="Rejected"

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    
    model_config = ConfigDict(from_attributes=True)

class JobCreate(BaseModel):
    company :str = Field(...)
    role : str = Field(...)
    status : JobStatus = JobStatus.INTERESTED

class JobOut(BaseModel):
    id: int
    company: str
    role: str
    status: JobStatus

    user_id: int 
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)