from pydantic import BaseModel, Field, ConfigDict
from enum import Enum

class JobStatus(str,Enum):
    INTERESTED = "Interested"
    APPLIED = "Applied"
    INTERVIEWING = "Interviewing"
    OFFER = "Offer"
    REJECTED ="Rejected"

class JobCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    company :str = Field(...)
    role : str = Field(...)
    status : JobStatus = JobStatus.INTERESTED

