# --------------------------------------USER-----------/api/v1/me---------------------------------------------------------------------------------
from fastapi import Depends, status
from sqlalchemy.orm import Session

from database.database import get_db
from schemas.schemas import UserInDBScheme, UserInScheme
from services import user_services

from fastapi import FastAPI
app = FastAPI()
v1 = FastAPI()
app.mount("/api/v1", v1)

@v1.post('/register', response_model=UserInScheme, status_code=status.HTTP_201_CREATED)
async def register_me(schema: UserInDBScheme, db: Session = Depends(get_db)):
    return user_services.create_user(db, schema)


@v1.get('/me', response_model=UserInScheme, status_code=status.HTTP_200_OK)
async def get_me(current_user: UserInScheme = Depends(user_services.get_current_is_active_user)):
    return current_user


@v1.put('/me', response_model=UserInScheme, status_code=status.HTTP_200_OK)
async def update_me(schema: UserInScheme, current_user: UserInScheme = Depends(user_services.get_current_is_active_user), db: Session = Depends(get_db)):
    return user_services.update_user(db, schema, current_user.email)


@v1.delete('/me', status_code=status.HTTP_204_NO_CONTENT)
async def delete_me(current_user: UserInScheme = Depends(user_services.get_current_is_active_user), db: Session = Depends(get_db)):
    return user_services.delete_user(db, current_user.email)
