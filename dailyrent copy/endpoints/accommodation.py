# --------------------------------------ACCOMMODATION--------/api/v1/accommodation----------------------------------------------------------------------------------
from fastapi import Depends, status
from sqlalchemy.orm import Session

from database.database import get_db
from models.enum import CityOfAccommodation, AccommodationCountry, TypeOfAccommodation
from schemas.schemas import AccommodationScheme, BaseAccommodationScheme, UserInScheme
from services.accommodation_services import accommodation_services
from services import user_services

from fastapi import FastAPI
app = FastAPI()
v1 = FastAPI()
app.mount("/api/v1", v1)

@v1.post('/accommodation', response_model=BaseAccommodationScheme, status_code=status.HTTP_201_CREATED)
async def create_accommodation(
                                type: TypeOfAccommodation,
                                city: CityOfAccommodation,
                                country: CountryOfAccommodation,
                                schema: BaseAccommodationScheme,
                                current_user: UserInScheme = Depends(user_services.get_current_is_active_user),
                                db: Session = Depends(get_db)):

    return accommodation_services.create_accommodation(db, schema, current_user, type, city, country)


@v1.get('/accommodation', status_code=status.HTTP_200_OK)
async def get_all_accommodations(current_user: UserInScheme = Depends(user_services.get_current_is_active_user)):
    return current_user.accommodations


@v1.get('/accommodation/{id}', status_code=status.HTTP_200_OK)
async def get_specify_accommodation(
                                id: int,
                                current_user: UserInScheme = Depends(user_services.get_current_is_active_user),
                                db: Session = Depends(get_db)):

    return accommodation_services.get_accommodation(db, id, current_user)


@v1.delete('/accommodation/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_specify_accommodation(
                                id: int,
                                current_user: UserInScheme = Depends(user_services.get_current_is_active_user),
                                db: Session = Depends(get_db)):

    return accommodation_services.delete_accommodation(db, id, current_user)


@v1.put('/accommodation/{id}', response_model=AccommodationScheme, status_code=status.HTTP_200_OK)
async def update_accommodation(
                                id: int,
                                type: TypeOfAccommodation,
                                city: CityOfAccommodation,
                                country: CountryOfAccommodation,
                                schema: AccommodationScheme,
                                current_user: UserInScheme = Depends(user_services.get_current_is_active_user),
                                db: Session = Depends(get_db)):

    return accommodation_services.update_accommodation(db, id, current_user, schema, type, city, country)
