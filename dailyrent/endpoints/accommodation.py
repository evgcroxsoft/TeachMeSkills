#________________________________________________________ACCOMMODATION__________________________________________________________________________________

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database.app_db import get_db
from models.enum import AccommodationCity, AccommodationCountry, AccommodationType
from schemas.schemas import AccommodationScheme, BaseAccommodationScheme, UserRetrieveScheme
from services.accommodation_service import accommodation_services
from services.user_service import user_services

router = APIRouter()

# ----------------------------------------------------/api/v1/accommodation----------------------------------------------------------------------------------

@router.post('/accommodation', response_model=BaseAccommodationScheme, status_code=status.HTTP_201_CREATED)
async def create_accommodation(
                                accommodation_type: AccommodationType,
                                city: AccommodationCity,
                                country: AccommodationCountry,
                                schema: BaseAccommodationScheme,
                                current_user: UserRetrieveScheme = Depends(user_services.get_current_is_active_user),
                                db: Session = Depends(get_db)):
    return await accommodation_services.create_accommodation(accommodation_type, city, country, schema, current_user, db)


@router.get('/accommodation', status_code=status.HTTP_200_OK)
async def get_all_accommodations(db: Session = Depends(get_db), current_user: UserRetrieveScheme = Depends(user_services.get_current_is_active_user)):
    return await accommodation_services.get_all_accommodations(db, current_user)


@router.get('/accommodation/{id}', status_code=status.HTTP_200_OK)
async def get_specify_accommodation(
                                id: int,
                                current_user: UserRetrieveScheme = Depends(user_services.get_current_is_active_user),
                                db: Session = Depends(get_db)):

    return await accommodation_services.get_accommodation(db, id, current_user)


@router.delete('/accommodation/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_specify_accommodation(
                                id: int,
                                current_user: UserRetrieveScheme = Depends(user_services.get_current_is_active_user),
                                db: Session = Depends(get_db)):

    return await accommodation_services.delete_accommodation(db, id, current_user)


@router.put('/accommodation/{id}', response_model=AccommodationScheme, status_code=status.HTTP_200_OK)
async def update_accommodation(
                                id: int,
                                accommodation_type: AccommodationType,
                                city: AccommodationCity,
                                country: AccommodationCountry,
                                schema: AccommodationScheme,
                                current_user: UserRetrieveScheme = Depends(user_services.get_current_is_active_user),
                                db: Session = Depends(get_db)):

    return await accommodation_services.update_accommodation(db, id, current_user, schema, accommodation_type, city, country)
