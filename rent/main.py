import uvicorn
from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session

from database.base import engine, SessionLocal

from models import models
from models.models import Landlord


from schema.appartment import AppartmentCreateSchema, AppartmentRetrieveSchema, AppartmentUpdateSchema
from schema.landlord import LandlordCreateSchema, LandlordRetrieveSchema, LandlordUpdateSchema
from schema.tenant import TenantCreateSchema, TenantRetrieveSchema, TenantUpdateSchema

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__":
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True)


@app.post('/landlord/', response_model=LandlordRetrieveSchema, status_code=status.HTTP_201_CREATED)
async def create(schema: LandlordCreateSchema, db: Session = Depends(get_db)):
    async def retrieve_landlord_by_email(db, email: str):
        return db.query(Landlord).filter_by(email=email).first()

    landlord = await retrieve_landlord_by_email(db, schema.dict()['email'])
    if landlord:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Landlord already exists.')

    
    async def create_landlord(db, schema):
        landlord = Landlord(**schema.dict())

        db.add(landlord)
        db.commit()
        db.refresh(landlord)

    landlord = await create_landlord(db, schema)
    return landlord