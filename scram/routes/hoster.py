from uuid import UUID
from fastapi import BackgroundTasks, Depends, status
from sqlalchemy.orm import Session
from schemas import schemas
from database.database import get_db
from services import services, tasks
from main import app
from services import security


@app.get("/hoster/{id}", response_model=schemas.HosterRetrieve)
async def get_host(id: UUID, db: Session = Depends(get_db)):
    return await services.get_host(db, id)


@app.post("/hoster/", response_model=schemas.HosterRetrieve, status_code=status.HTTP_201_CREATED)
async def create_host(schema: schemas.HosterCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    await services.check_host(db, schema)
    background_tasks.add_task(tasks.send_email)
    return await services.create_host(db, schema)


@app.put("/hoster/{id}", response_model=schemas.HosterRetrieve, status_code=status.HTTP_200_OK)
async def update_host(id: UUID, schema: schemas.HosterUpdate, db: Session = Depends(get_db)):
    host = await services.get_host(db, id)
    return await services.update_host(db, host, schema)


@app.delete("/hoster/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_host(id: UUID, db: Session = Depends(get_db)):
    return await services.delete_host(db, id)
