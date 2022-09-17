from base64 import b64encode
from datetime import datetime, date, timedelta
from enum import Enum
from jose import JWTError, jwt
from fastapi import FastAPI, Depends, HTTPException, status, BackgroundTasks
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr
from secrets import token_bytes
from sqlalchemy import create_engine, Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session
from sqlalchemy_utils import UUIDType
import uvicorn
import uuid

import tasks

# ________________________________________________________MAIN.PY__________________________________________________________________________________

# create instance FastAPI
app = FastAPI()
v1 = FastAPI()
app.mount("/api/v1", v1)


if __name__ == "__main__":
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True)

# ________________________________________________________DATABASE__________________________________________________________________________________


SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ________________________________________________________MODELS__________________________________________________________________________________

# ---------------------------------------------------------Enum----------------------------------------------------------------------------------


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

# ---------------------------------------------------------Models----------------------------------------------------------------------------------


class DataBase(Base):
    __abstract__ = True
    created_at = Column(Date, default=datetime.date)


class User(DataBase):
    __tablename__ = 'users'

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4())
    email = Column(String(100), unique=True, nullable=False)
    first_name = Column(String(50))
    last_name = Column(String(100))
    telephone = Column(String(20))
    hashed_password = Column(String(100), nullable=False)
    renter = Column(Boolean, default=False)
    hoster = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    accommodations = relationship('Accommodation', backref='users', cascade='all, delete')
    bookings = relationship('Booking', backref='users')


class Accommodation(DataBase):
    __tablename__ = 'accommodations'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    persons = Column(Integer)
    is_active = Column(Boolean, default=True)
    type = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)
    price = Column(Integer)
    user_id = Column(UUIDType(binary=False), ForeignKey('users.id'))
    # price_id = Column(Integer, ForeignKey('prices.id'))

    # users = relationship('User', back_populates='accommodations')


class Booking(DataBase):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    date_start = Column(Date, nullable=False)
    date_end = Column(Date, nullable=False)
    persons = Column(Integer)
    status = Column(String(100))
    price = Column(Integer)
    user_id = Column(UUIDType(binary=False), ForeignKey('users.id'))
    accommodation_id = Column(Integer, ForeignKey('accommodations.id'))


class RenterFeedback(DataBase):
    __tablename__ = 'renter_feedbacks'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    description = Column(String(200), nullable=False)
    rating = Column(Integer)
    booking_id = Column(Integer, ForeignKey('accommodations.id'))
    user_id = Column(UUIDType(binary=False), ForeignKey('users.id'))


class HosterFeedback(DataBase):
    __tablename__ = 'hoster_feedbacks'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    description = Column(String(200), nullable=False)
    rating = Column(Integer)
    booking_id = Column(Integer, ForeignKey('accommodations.id'))
    user_id = Column(UUIDType(binary=False), ForeignKey('users.id'))


# create all tables, this line need to be after models
Base.metadata.create_all(bind=engine)

# ________________________________________________________SCHEMAS__________________________________________________________________________________

# ---------------------------------------------------------Base----------------------------------------------------------------------------------


class BaseUserScheme(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    telephone: str | None = None
    renter: bool = False
    hoster: bool = False
    is_active: bool
    created_at: date

    class Config:
        orm_mode = True

# ----------------------------------------------------------User----------------------------------------------------------------------------------


class UserInScheme(BaseUserScheme):
    update_at: date | None = None

    class Config:
        orm_mode = True


class UserInDBScheme(BaseUserScheme):
    hashed_password: str

    class Config:
        orm_mode = True

# ---------------------------------------------------------Accommodation---------------------------------------------------------------------------------


class BaseAccommodationScheme(BaseModel):
    name: str
    persons: int
    is_active: bool
    created_at: date
    type: str | None = None
    city: str | None = None
    country: str | None = None
    price: int

    class Config:
        orm_mode = True


class AccommodationScheme(BaseAccommodationScheme):
    update_at: date | None = None

    class Config:
        orm_mode = True

# ---------------------------------------------------------Booking---------------------------------------------------------------------------------


class BaseBookingScheme(BaseModel):
    date_start: date
    date_end: date
    persons: int
    created_at: date
    status: str
    accommodation_id: int

    class Config:
        orm_mode = True


class BookingScheme(BaseBookingScheme):
    update_at: date | None = None
    price: int | None = None

    class Config:
        orm_mode = True


# ---------------------------------------------------------Feedbacks---------------------------------------------------------------------------------

class BaseFeedbackScheme(BaseModel):
    description: str
    rating: int
    booking_id: int
    created_at: date

    class Config:
        orm_mode = True


class FeedbackScheme(BaseFeedbackScheme):
    update_at: date | None = None

    class Config:
        orm_mode = True


class RenterFeedbackScheme(BaseFeedbackScheme):
    renter_id: uuid.UUID

    class Config:
        orm_mode = True

class HosterFeedbackScheme(BaseFeedbackScheme):
    hoster_id: uuid.UUID

    class Config:
        orm_mode = True

class CreateFeedbackScheme(HosterFeedbackScheme, RenterFeedbackScheme):
    pass

    class Config:
        orm_mode = True


# ---------------------------------------------------------Token---------------------------------------------------------------------------------


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None


# ________________________________________________________SECURITY__________________________________________________________________________________

# -------------------------------------------------Hashing and Verify Password---------------------------------------------------------------------------------


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# -------------------------------------------------Oauth2---------------------------------------------------------------------------------

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# -------------------------------------------------JWT Token---------------------------------------------------------------------------------

SECRET_KEY = b64encode(token_bytes(32)).decode()
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@v1.post("/token", response_model=Token)
async def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = user_services.authenticate_user(
        db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


# ________________________________________________________SERVICES__________________________________________________________________________________

# -------------------------------------------------UserServices---------------------------------------------------------------------------------

class UserServices():

    def check_host(self, db, email):
        if db.query(User).filter_by(email=email).first():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail='Host already exists')

    def create_user(self, db, schema):
        data = schema.dict()
        self.check_host(db, data['email'])
        data['hashed_password'] = get_password_hash(
            schema.dict()['hashed_password'])
        user = User(**data)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def update_user(self, db, schema, email):
        user = self.get_user(db, email)
        for key, value in schema.dict().items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
        return user

    def get_user(self, db, email):
        user = db.query(User).filter_by(email=email).first()
        if user:
            return user

    def delete_user(self, db, email):
        user = self.get_user(db, email)
        db.delete(user)
        db.commit()
        raise HTTPException(status_code=status.HTTP_200_OK,
                            detail='Host was deleted successfully')

    def authenticate_user(self, db, email: str, password: str):
        user = self.get_user(db, email)
        if not user:
            return False
        if not verify_password(password, user.hashed_password):
            return False
        return user

    async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            email: str = payload.get("sub")
            if email is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception
        user = user_services.get_user(db, email)
        if user is None:
            raise credentials_exception
        return user

    async def get_current_is_active_user(db: Session = Depends(get_db), current_user: UserInScheme = Depends(get_current_user)):
        if current_user.is_active == False:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user


user_services = UserServices()

# -------------------------------------------------AccommodationServices---------------------------------------------------------------------------------


class AccommodationServices():

    def create_accommodation(self, db, schema, current_user, type, city, country):
        if current_user.hoster:
            data = schema.dict()
            data['user_id'] = current_user.id
            data['type'] = type
            data['city'] = city
            data['country'] = country
            user = Accommodation(**data)
            db.add(user)
            db.commit()
            db.refresh(user)
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="No rights to create accommodations")
        return user

    def get_accommodation(self, db, id, current_user):
        accommodation = db.query(Accommodation).filter_by(
            user_id=current_user.id).filter_by(id=id).first()
        return accommodation

    def update_accommodation(self, db, id, current_user, schema, type, city, country):
        data = schema.dict()
        data['type'] = type
        data['city'] = city
        data['country'] = country
        accommodation = self.get_accommodation(db, id, current_user)
        for key, value in data.items():
            setattr(accommodation, key, value)
        db.commit()
        db.refresh(accommodation)
        return accommodation

    def delete_accommodation(self, db, id, current_user):
        specify_accommodation = db.query(Accommodation).filter_by(
            user_id=current_user.id).filter_by(id=id).first()
        db.delete(specify_accommodation)
        db.commit()
        raise HTTPException(status_code=status.HTTP_200_OK,
                            detail='Specify accommodation was deleted successfully')


    def searching_accommodations(self, date_start, date_end, type, persons, city, country, db):
        filtered_accommodation = []
        accommodation_in_db = db.query(Accommodation).all()

        for accommodation in accommodation_in_db:

            if accommodation.country == country or country == None:

                if accommodation.city == city or city == None:

                    if accommodation.type == type or type == None:

                        if accommodation.persons == persons or persons == None:
                            
                            if booking_services.check_is_available_booking(db, accommodation.id, date_start, date_end):
                                filtered_accommodation.append(accommodation)
        if filtered_accommodation == []:
            raise HTTPException(status_code=status.HTTP_200_OK, detail='Sorry but no free accommodation')
        return filtered_accommodation    


accommodation_services = AccommodationServices()


# -------------------------------------------------BookingServices---------------------------------------------------------------------------------

class BookingServices():

    def create_booking(self, db, schema, current_user, background_tasks):
        '''
        Check and compare dates, if ok
        '''
        if current_user.renter:
            data = schema.dict()
            if self.check_is_available_booking(db, data['accommodation_id'], data['date_start'], data['date_end']) == True or None:
                accommodation = db.query(Accommodation).filter_by(id=data['accommodation_id']).first()
                data['user_id'] = current_user.id
                data['price'] = accommodation.price
                data['status'] = BookingStatus.waiting
                user = Booking(**data)
                db.add(user)
                db.commit()
                db.refresh(user)
                background_tasks.add_task(tasks.send_email)
                return user
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No dates to create bookings, choose another")        
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No rights to create bookings")


    def get_booking(self, db, id, current_user):
        booking = db.query(Booking).filter_by(
            user_id=current_user.id).filter_by(id=id).first()
        return booking

    def update_booking(self, db, id, current_user, schema):
        data = schema.dict()
        booking = self.get_booking(db, id, current_user)
        for key, value in data.items():
            setattr(booking, key, value)
        db.commit()
        db.refresh(booking)
        return booking

    def delete_booking(self, db, id, current_user):
        specify_booking = db.query(Booking).filter_by(
            user_id=current_user.id).filter_by(id=id).first()
        if specify_booking.status == BookingStatus.waiting:
            db.delete(specify_booking)
            db.commit()
            raise HTTPException(status_code=status.HTTP_200_OK,
                                detail='Specify booking was deleted successfully')

    def check_dates_booking(self, b1, b2, s1, s2):
        booking_period = [b1 + timedelta(days=x) for x in range((b2-b1).days + 1)]
        searching_period = [s1 + timedelta(days=x) for x in range((s2-s1).days + 1)]
        for book in booking_period:
            for search in searching_period:
                if book == search:
                    return True


    def check_status_booking(self, status, bookings_db):
        filtered_booking = []
        for booking in bookings_db:
            if booking.status == status or status == None:
                filtered_booking.append(booking)
        return filtered_booking

    def check_is_available_booking(self, db, accommodation_id, searching_date_start, searching_date_end):
        '''
        Func returns True if booking is available for searching:
        '''
        booking_in_db = db.query(Booking).filter_by(accommodation_id=accommodation_id).all()

        if booking_in_db == []: # if accommodation hasn't any bookings
            return True

        result = []
        for booking in booking_in_db:

            if booking.status == BookingStatus.declined or booking.status == BookingStatus.finished:
                return True

            elif booking.status == BookingStatus.waiting or booking.status == BookingStatus.approved:
                compare_dates = self.check_dates_booking(booking.date_start, booking.date_end, searching_date_start, searching_date_end)
                result.append(compare_dates) # create list of all compare_dates True and False

            for bool in result:
                if bool == True: return False # Rerurn True if booking with status waiting or approved has the dates are not free

booking_services = BookingServices()



# -------------------------------------------------FeedbackServices---------------------------------------------------------------------------------

class FeedbackServices():

    def create_feedback(self, db, schema, current_user, rating, background_tasks):
        '''
        Func check Renter or Hoster and store feedback in DB
        '''
        data = schema.dict()
        booking_in_db = db.query(Booking).filter_by(id=data['booking_id']).first()
        if booking_in_db:
            if self.feedback_create_if_renter(db, data, current_user, booking_in_db, background_tasks, rating):
                pass
            else: 
                self.feedback_create_if_hoster(db, data, current_user, booking_in_db, background_tasks, rating)
        else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No booking in db")


    def feedback_create_if_renter(self, db, data, current_user, booking_in_db, background_tasks, rating):
        '''
        Func check Renter and save data in table RenterFeedback:
        1. Is it your booking?
        2. Is booking status is finished?
        3. Have you left your review before?
        '''
        if current_user.renter:
            if booking_in_db.user_id == current_user.id:
                if booking_in_db.status == BookingStatus.finished:
                    if db.query(RenterFeedback).filter_by(user_id=current_user.id).filter_by(booking_id=booking_in_db.id).first():
                        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="You have already leaved feedback")
                    else:
                        data['user_id'] = current_user.id
                        data['rating'] = rating
                        feedback = RenterFeedback(**data)
                        db.add(feedback)
                        db.commit()
                        db.refresh(feedback)
                        background_tasks.add_task(tasks.send_email)
                        return feedback
                else:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Booking status not finished")
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No rights to create feedback")   


    def feedback_create_if_hoster(self, db, data, current_user, booking_in_db, background_tasks, rating):
        '''
        Func check Hoster and save data in table HosterFeedback:
        1. Is this booking related to your accommodation?
        2. Is booking status is finished?
        3. Have you left your review before?
        '''
        if current_user.hoster: 
            if db.query(Booking, Accommodation).join(Accommodation).filter_by(id=booking_in_db.id).filter_by(user_id=current_user.id).first():  
                if booking_in_db.status == BookingStatus.finished:
                    if db.query(HosterFeedback).filter_by(user_id=current_user.id).filter_by(booking_id=booking_in_db.id).first():
                        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="You have already leaved feedback")
                    else:
                        data['user_id'] = current_user.id
                        data['rating'] = rating
                        feedback = HosterFeedback(**data)
                        db.add(feedback)
                        db.commit()
                        db.refresh(feedback)
                        background_tasks.add_task(tasks.send_email)
                        return feedback
                else:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Booking status not finished")
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No rights to create feedback")  


feedback_services = FeedbackServices()


# ________________________________________________________ENDPOINTS__________________________________________________________________________________


@v1.get('/searching', status_code=status.HTTP_200_OK) #TODO:response_model=without ID, and 
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

# --------------------------------------USER-----------/api/v1/me---------------------------------------------------------------------------------


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

# --------------------------------------ACCOMMODATION--------/api/v1/accommodation----------------------------------------------------------------------------------


@v1.post('/accommodation', response_model=BaseAccommodationScheme, status_code=status.HTTP_201_CREATED)
async def create_accommodation(
        type: TypeOfAccommodation,
        city: CityOfAccommodation,
        country: CountryOfAccommodation,
        schema: BaseAccommodationScheme,
        current_user: UserInScheme = Depends(
            user_services.get_current_is_active_user),
        db: Session = Depends(get_db)):

    return accommodation_services.create_accommodation(db, schema, current_user, type, city, country)


@v1.get('/accommodation', status_code=status.HTTP_200_OK)
async def get_all_accommodations(current_user: UserInScheme = Depends(user_services.get_current_is_active_user)):
    return current_user.accommodations


@v1.get('/accommodation/{id}', status_code=status.HTTP_200_OK)
async def get_specify_accommodation(
        id: int,
        current_user: UserInScheme = Depends(
            user_services.get_current_is_active_user),
        db: Session = Depends(get_db)):

    return accommodation_services.get_accommodation(db, id, current_user)


@v1.delete('/accommodation/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_specify_accommodation(
        id: int,
        current_user: UserInScheme = Depends(
            user_services.get_current_is_active_user),
        db: Session = Depends(get_db)):
    return accommodation_services.delete_accommodation(db, id, current_user)


@v1.put('/accommodation/{id}', response_model=AccommodationScheme, status_code=status.HTTP_200_OK)
async def update_accommodation(
        id: int,
        type: TypeOfAccommodation,
        city: CityOfAccommodation,
        country: CountryOfAccommodation,
        schema: AccommodationScheme,
        current_user: UserInScheme = Depends(
            user_services.get_current_is_active_user),
        db: Session = Depends(get_db)):

    return accommodation_services.update_accommodation(db, id, current_user, schema, type, city, country)

# --------------------------------------BOOKING--------/api/v1/booking----------------------------------------------------------------------------------


@v1.post('/booking', response_model=BookingScheme, status_code=status.HTTP_201_CREATED)
async def create_booking(
        background_tasks: BackgroundTasks, 
        schema: BaseBookingScheme,
        current_user: UserInScheme = Depends(
            user_services.get_current_is_active_user),
        db: Session = Depends(get_db)):

    return booking_services.create_booking(db, schema, current_user, background_tasks)


@v1.get('/booking', status_code=status.HTTP_200_OK)
async def get_all_bookings(status: BookingStatus | None = None, current_user: UserInScheme = Depends(user_services.get_current_is_active_user)):
    return booking_services.check_status_booking(status, current_user.bookings)


@v1.get('/booking/{id}', status_code=status.HTTP_200_OK)
async def get_specify_booking(
        id: int,
        current_user: UserInScheme = Depends(
            user_services.get_current_is_active_user),
        db: Session = Depends(get_db)):

    return booking_services.get_booking(db, id, current_user)


@v1.delete('/booking/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_specify_booking(
        id: int,
        current_user: UserInScheme = Depends(
            user_services.get_current_is_active_user),
        db: Session = Depends(get_db)):
    return booking_services.delete_booking(db, id, current_user)


@v1.put('/booking/{id}', response_model=BookingScheme, status_code=status.HTTP_200_OK)
async def update_booking(
        id: int,
        schema: BookingScheme,
        current_user: UserInScheme = Depends(
            user_services.get_current_is_active_user),
        db: Session = Depends(get_db)):

    return booking_services.update_booking(db, id, current_user, schema)


# -------------------------------------FEEDBACK--------/api/v1/feedback----------------------------------------------------------------------------------

@v1.post('/feedback', status_code=status.HTTP_201_CREATED)
async def create_feedback(
                        rating: FeedbackRating,
                        background_tasks: BackgroundTasks, 
                        schema: BaseFeedbackScheme,
                        current_user: UserInScheme = Depends(user_services.get_current_is_active_user),
                        db: Session = Depends(get_db)):
    return feedback_services.create_feedback(db, schema, current_user, rating, background_tasks)