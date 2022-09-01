from fastapi import BackgroundTasks, Depends, status
from sqlalchemy.orm import Session
from schemas import schemas
from database.database import get_db
from services import services, tasks
from main import app


@app.get("/{id}", response_model=schemas.RetrieveHost)
async def read_host(id: int, db: Session = Depends(get_db)):
    return await services.get_host(db, id)


@app.post("/", response_model=schemas.RetrieveHost, status_code=status.HTTP_201_CREATED)
async def create_host(schema: schemas.CreateHost, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    await services.check_host(db, schema)
    background_tasks.add_task(tasks.send_email)
    return await services.create_host(db, schema)


@app.put("/{id}", response_model=schemas.RetrieveHost, status_code=status.HTTP_200_OK)
async def update_host(id: int, schema: schemas.UpdateHost, db: Session = Depends(get_db)):
    host = await services.get_host(db, id)
    return await services.update_host(db, host, schema)


@app.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_host(id: int, db: Session = Depends(get_db)):
    return await services.delete_host(db, id)
