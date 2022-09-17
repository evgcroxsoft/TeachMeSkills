#________________________________________________________ENUM__________________________________________________________________________________

from enum import Enum


class AccommodationType(Enum):
    FLAT = 'Flat'
    HOUSE = 'House'
    VILLA = 'Villa'
    HOTEL = 'Hotel'


class AccommodationCountry(Enum):
    ARGENTINA = 'Argentina'
    SPAIN = 'Spain'
    NETHERLANDS = 'Netherlands'
    POLAND = 'Poland'


class AccommodationCity(Enum):
    MADRID = 'Madrid'
    AMSTERDAM = 'Amsterdam'
    WARSAWA = 'Warsawa'
    BUDAPEST = 'Budapest'


class BookingStatus(Enum):
    WAITING = 'waiting'
    APPROVED = 'approved'
    DECLINED = 'declined'
    FINISHED = 'finished'


class FeedbackRating(Enum):
    VERY_BAD = 1
    BAD = 2
    SO_SO = 3
    GOOD = 4
    BEST = 5
