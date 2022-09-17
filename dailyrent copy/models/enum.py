from enum import Enum


class TypeOfAccommodation(str, Enum):
    flat = 'Flat'
    house = 'House'
    villa = 'Villa'
    hotel = 'Hotel'


class CountryOfAccommodation(str, Enum):
    argentina = 'Argentina'
    spania = 'Spain'
    netherlands = 'Netherlands'
    poland = 'Poland'


class CityOfAccommodation(str, Enum):
    madrid = 'Madrid'
    amsterdam = 'Amsterdam'
    warsawa = 'Warsawa'
    budapest = 'Budapest'


class BookingStatus(str, Enum):
    waiting = 'waiting'
    approved = 'approved'
    declined = 'declined'
    finished = 'finished'


class FeedbackRating(str, Enum):
    very_bad = 1
    bad = 2
    so_so = 3
    good = 4
    best = 5
