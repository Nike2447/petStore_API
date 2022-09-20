from fastapi import FastAPI, Depends, Response, status, HTTPException
import schemas, models
from database import engine, SessionLocal
from sqlalchemy.orm import Session 

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  


@app.post('/petStore')                                                  #decorator to create new information
def create(request : schemas.info,db : Session = Depends(get_db) ):
    new_info = models.info(petName = request.petName,ownerName = request.ownerName,age = request.age,type = request.type, gender = request.gender)
    db.add(new_info)
    db.commit()
    db.refresh(new_info)
    return new_info

@app.get('/petStore')                                                   #decorator to display information
def show(db : Session = Depends(get_db)):
    info = db.query(models.info).all()
    return info

@app.put('/petStore/{id}',status_code = status.HTTP_202_ACCEPTED)       #decorator to update information
def update(id,request: schemas.info,db : Session = Depends(get_db)):
    info = db.query(models.info).filter(models.info.id == id)
    if not info.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Information with id {id} not found in database!')
    info.update(request.dict(),synchronize_session=False)
    db.commit()
    return 'Updation successfull'

@app.delete('/petStore/{id}',status_code=status.HTTP_204_NO_CONTENT)    #decorator to delete information
def destroy(id,db : Session = Depends(get_db)):
    info = db.query(models.info).filter(models.info.id == id)
    if not info.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Information with id {id} not found in database")
    info.delete(synchronize_session=False)
    db.commit()
    return 'Successfully deleted information'

