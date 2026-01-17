from pydantic import BaseModel, EmailStr
from typing import Optional
from app import models


# Shared fields (NO id here)
class StudentBase(BaseModel):
    name: str
    age: int
    email: EmailStr
    phone: str


# Used for POST /students
class StudentCreate(StudentBase):
    pass


# Used for PUT/PATCH /students/{id}
class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None


# Used for responses (includes id)
class StudentResponse(StudentBase):
    id: int

    class Config:
        from_attributes = True
