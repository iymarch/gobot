from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Date, DateTime, Enum

from database import Base
from models.schemas import TypeCall


class Course(Base):
    __tablename__ = "courses"

    course_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    create_date = Column(DateTime, default=datetime.utcnow)
    visible = Column(Boolean, default=1)
    start_date = Column(DateTime)
    finish_date = Column(DateTime)
    key = Column(String, unique=True)
    creator_id = Column(Integer)
