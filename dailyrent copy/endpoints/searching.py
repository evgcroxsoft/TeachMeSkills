# --------------------------------------SEARCHING-----------/api/v1/searching---------------------------------------------------------------------------------
from datetime import date
from fastapi import Depends, status
from sqlalchemy.orm import Session

from database.database import get_db
from models.enum import CityOfAccommodation, CountryOfAccommodation, TypeOfAccommodation
from services.accommodation_services import accommodation_services

from fastapi import FastAPI
app = FastAPI()
v1 = FastAPI()
app.mount("/api/v1", v1)

@v1.post('/searching', status_code=status.HTTP_200_OK) #TODO:response_model=without ID, and 
async def searching_accommodations(
                                    date_start: date,
                                    date_end: date,
                                    country: CountryOfAccommodation | None = None,
                                    city: CityOfAccommodation | None = None,
                                    type: TypeOfAccommodation | None = None,
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

    return accommodation_services.searching_accommodations(date_start, date_end, type, persons, city, country, db)
