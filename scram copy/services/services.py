from fastapi import status, HTTPException
from models import models


async def create_host(db, schema):
    db_host = models.Host(**schema.dict())
    db.add(db_host)
    db.commit()
    db.refresh(db_host)
    return db_host


async def check_host(db, schema):
    if db.query(models.Host).filter_by(email=schema.dict()['email']).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='Host already exists')


async def update_host(db, host, schema):
    for key, value in schema.dict().items():
        setattr(host, key, value)
    db.commit()
    db.refresh(host)
    return host


async def get_host(db, id: int):
    host = db.query(models.Host).filter_by(id=id).first()
    if host:
        return host
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail='Host does not exist')


async def delete_host(db, id) -> None:
    if host := await get_host(db, id):
        db.delete(host)
        db.commit()
        raise HTTPException(status_code=status.HTTP_200_OK,
                            detail='Host was deleted successfully')
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Host does not exist')
