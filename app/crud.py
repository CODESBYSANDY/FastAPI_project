from sqlalchemy.orm import Session
from app import models
from app.schemas import StudentCreate, StudentUpdate



    
def create_students(db: Session, student: StudentCreate):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
def get_students(db:Session,skip:int =0,limit:int =10,age=None):

    query = db.query(models.Student)

    if age is not None:
        query = query.filter(models.Student.age == age)

    return query.offset(skip).limit(limit).all()

def get_student(db:Session, student_id :int):
    db_student=db.query(models.Student).filter(models.Student.id==student_id).first()
    if not db_student:
        return None

    return db_student
def update_student(db:Session,student_id:int,updated_student:StudentUpdate):
    db_student= get_student (db,student_id)
    if not db_student:
        return None
    for key,value in updated_student.dict(exclude_unset=True).items():

      setattr(db_student,key,value)

    db.commit()
    db.refresh(db_student)
    return db_student

    
def delete_student(db:Session,student_id:int):
    db_student=get_student (db,student_id)
    if not db_student:
        return None
    db.delete(db_student)
    db.commit()
    return db_student