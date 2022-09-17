#________________________________________________________USER__________________________________________________________________________________

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database.app_db import get_db
from schemas.schemas import BaseUserScheme, UserCreateScheme, UserRetrieveScheme
from services.user_service import user_services

router = APIRouter()

# -----------------------------------------------------/api/v1/me---------------------------------------------------------------------------------

@router.post('/register', response_model=BaseUserScheme, status_code=status.HTTP_201_CREATED)
async def register_me(schema: UserCreateScheme, db: Session = Depends(get_db)):
    return await user_services.create_user(db, schema)


@router.get('/me', response_model=UserRetrieveScheme, status_code=status.HTTP_200_OK)
async def get_me(current_user: BaseUserScheme = Depends(user_services.get_current_is_active_user)):
    return current_user


@router.put('/me', response_model=UserRetrieveScheme, status_code=status.HTTP_200_OK)
async def update_me(schema: BaseUserScheme, current_user: UserRetrieveScheme = Depends(user_services.get_current_is_active_user), db: Session = Depends(get_db)):
    return await user_services.update_user(db, schema, current_user.email)


@router.delete('/me', status_code=status.HTTP_204_NO_CONTENT)
async def delete_me(current_user: UserRetrieveScheme = Depends(user_services.get_current_is_active_user), db: Session = Depends(get_db)):
    return await user_services.delete_user(db, current_user.email)

