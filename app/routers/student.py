from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional

from app.database import SessionLocal
from app.schemas import StudentCreate, StudentUpdate, StudentResponse
from app import crud


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE
@router.post("/", response_model=StudentResponse)
def create(student: StudentCreate, db: Session = Depends(get_db)):
    return crud.create_students(db, student)


@router.get("/", response_model=list[StudentResponse])
def get_all(
    age: Optional[int] = None,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    user: str = Depends(get_db)   # 🔐 PROTECTED
):
    return crud.get_students(db, skip=skip, limit=limit, age=age)
# READ ONE
@router.get("/{student_id}", response_model=StudentResponse)
def get_one(student_id: int, db: Session = Depends(get_db)):
    student_db = crud.get_student(db, student_id)
    if not student_db:
        raise HTTPException(status_code=404, detail="Student not found")
    return student_db


# UPDATE
@router.put("/{student_id}", response_model=StudentResponse)
def update(
    student_id: int,
    updated_student: StudentUpdate,
    db: Session = Depends(get_db)
):
    student_db = crud.update_student(db, student_id, updated_student)
    if not student_db:
        raise HTTPException(status_code=404, detail="Student not found")
    return student_db


# DELETE
@router.delete("/{student_id}")
def delete(student_id: int, db: Session = Depends(get_db)):
    student_db = crud.delete_student(db, student_id)
    if not student_db:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}
