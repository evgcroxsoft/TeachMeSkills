#________________________________________________________SEARCHING__________________________________________________________________________________

from datetime import date
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database.app_db import get_db
from models.enum import AccommodationCity, AccommodationCountry, AccommodationType
from services.accommodation_service import accommodation_services


router = APIRouter()

# --------------------------------------------------/api/v1/searching---------------------------------------------------------------------------------

@router.post('/searching', status_code=status.HTTP_200_OK) 
async def searching_accommodations(
                                    date_start: date,
                                    date_end: date,
                                    country: AccommodationCountry | None = None,
                                    city: AccommodationCity | None = None,
                                    accommodation_type: AccommodationType | None = None,
                                    persons: int | None = None, 
                                    db: Session = Depends(get_db)):
    '''
        Func returns all accommodation:
        - without filters;
        - filtered by country;
        - filteredf by city;
        - filtered by type of accommodation;
        - filtered by persons;
        - filtered all available for status code (waiting and approved go in);
        - filtered all available for the searching dates
    '''

    return await accommodation_services.searching_accommodations(date_start, date_end, country, city, accommodation_type, persons, db)
