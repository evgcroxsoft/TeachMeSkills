#________________________________________________________BOOKING__________________________________________________________________________________

from fastapi import APIRouter, Depends, status, BackgroundTasks
from sqlalchemy.orm import Session

from database.app_db import get_db
from models.enum import BookingStatus
from schemas.schemas import BaseBookingScheme, BookingScheme, UserRetrieveScheme
from services.booking_service import booking_services
from services.user_service import user_services

router = APIRouter()


# ----------------------------------------------------/api/v1/booking----------------------------------------------------------------------------------

@router.post('/booking', response_model=BookingScheme, status_code=status.HTTP_201_CREATED)
async def create_booking(
                        background_tasks: BackgroundTasks, 
                        schema: BaseBookingScheme,
                        current_user: UserRetrieveScheme = Depends(user_services.get_current_is_active_user),
                        db: Session = Depends(get_db)):

    return await booking_services.create_booking(db, schema, current_user, background_tasks)


@router.get('/booking', status_code=status.HTTP_200_OK)
async def get_all_bookings(status: BookingStatus | None = None, current_user: UserRetrieveScheme = Depends(user_services.get_current_is_active_user)):
    return await booking_services.check_status_booking(status, current_user.bookings)


@router.get('/booking/{id}', status_code=status.HTTP_200_OK)
async def get_specify_booking(
                        id: int,
                        current_user: UserRetrieveScheme = Depends(user_services.get_current_is_active_user),
                        db: Session = Depends(get_db)):

    return await booking_services.get_booking(db, id, current_user)


@router.delete('/booking/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_specify_booking(
                        id: int,
                        current_user: UserRetrieveScheme = Depends(user_services.get_current_is_active_user),
                        db: Session = Depends(get_db)):
    return await booking_services.delete_booking(db, id, current_user)


@router.put('/booking/{id}', response_model=BookingScheme, status_code=status.HTTP_200_OK)
async def update_booking(
                        id: int,
                        schema: BookingScheme,
                        current_user: UserRetrieveScheme = Depends(user_services.get_current_is_active_user),
                        db: Session = Depends(get_db)):

    return await booking_services.update_booking(db, id, current_user, schema)
