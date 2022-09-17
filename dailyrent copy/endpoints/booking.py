# --------------------------------------BOOKING--------/api/v1/booking----------------------------------------------------------------------------------
from fastapi import Depends, status, BackgroundTasks
from sqlalchemy.orm import Session

from database.database import get_db
# from main import app, v1
from models.enum import BookingStatus
from schemas.schemas import BaseBookingScheme, BookingScheme, UserInScheme
from services.booking_services import booking_services
from services import user_services

from fastapi import FastAPI
app = FastAPI()
v1 = FastAPI()
app.mount("/api/v1", v1)


@v1.post('/booking', response_model=BookingScheme, status_code=status.HTTP_201_CREATED)
async def create_booking(
                        background_tasks: BackgroundTasks, 
                        schema: BaseBookingScheme,
                        current_user: UserInScheme = Depends(user_services.get_current_is_active_user),
                        db: Session = Depends(get_db)):

    return booking_services.create_booking(db, schema, current_user, background_tasks)


@v1.get('/booking', status_code=status.HTTP_200_OK)
async def get_all_bookings(status: BookingStatus | None = None, current_user: UserInScheme = Depends(user_services.get_current_is_active_user)):
    return booking_services.check_status_booking(status, current_user.bookings)


@v1.get('/booking/{id}', status_code=status.HTTP_200_OK)
async def get_specify_booking(
                        id: int,
                        current_user: UserInScheme = Depends(user_services.get_current_is_active_user),
                        db: Session = Depends(get_db)):

    return booking_services.get_booking(db, id, current_user)


@v1.delete('/booking/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_specify_booking(
                        id: int,
                        current_user: UserInScheme = Depends(user_services.get_current_is_active_user),
                        db: Session = Depends(get_db)):
    return booking_services.delete_booking(db, id, current_user)


@v1.put('/booking/{id}', response_model=BookingScheme, status_code=status.HTTP_200_OK)
async def update_booking(
                        id: int,
                        schema: BookingScheme,
                        current_user: UserInScheme = Depends(user_services.get_current_is_active_user),
                        db: Session = Depends(get_db)):

    return booking_services.update_booking(db, id, current_user, schema)
