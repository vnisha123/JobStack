from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint,DateTime,func
from app.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    jobs = relationship("Job", back_populates="owner", cascade="all, delete-orphan")


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, nullable=False)
    role = Column(String, nullable=False)
    status = Column(String, default="Applied")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(Integer, ForeignKey("users.id",ondelete="CASCADE"), nullable=False)
    owner = relationship("User", back_populates="jobs")

    __table_args__ = (
        UniqueConstraint('user_id','company', 'role', name='_user_company_role_uc'),
    )