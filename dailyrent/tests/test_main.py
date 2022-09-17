# ________________________________________________________TESTS__________________________________________________________________________________

from fastapi.testclient import TestClient
from main import app
from database.app_db import engine, Base,sessionmaker, get_db,SessionLocal
from sqlalchemy import create_engine
from randominfo import random_password


client = TestClient(app)

# -------------------------------------------------Register User---------------------------------------------------------------------------------

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


import random
import string

def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


random_email = (random_char(7)+"@gmail.com")
random_first_name = (random_char(7))
random_last_name = (random_char(7))
random_password = random_password(length = 8, special_chars = True, digits = True)

def test_register():
    response = client.post("api/v1/register",json={
                                    "email": random_email,
                                    "first_name": random_first_name,
                                    "last_name": random_last_name,
                                    "phone": "380989878",
                                    "renter": bool(False),
                                    "hoster": bool(False),
                                    "is_active": bool(True),
                                    'created_at': '2022-10-01',
                                    "hashed_password": random_password
                                    })
    assert response.status_code == 201
    data = response.json()
    assert data["first_name"] == random_first_name
    assert data["last_name"] == random_last_name
    assert data["email"] == random_email
    
    token(random_email, random_password)



    app.dependency_overrides.clear()

# -------------------------------------------------Token---------------------------------------------------------------------------------

def token(email, password):
    response = client.post("api/v1/token", 
                                        {
                                        "username": email,
                                        "password": password
                                        })
    data = response.json()
    access_token = data['access_token']
    response = client.get("api/v1/me", headers = {"Authorization": f"Bearer {access_token}"})
    assert response.status_code == 200


# -------------------------------------------------GET User---------------------------------------------------------------------------------



# -------------------------------------------------GET Searching---------------------------------------------------------------------------------

def test_searching():
    response = client.post("api/v1/searching", params={
                                        'date_start': "2022-10-01", 
                                        'date_end': "2022-10-10", 
                                        'country': None,
                                        'city': None,
                                        'type': None,
                                        'person': None
                                        })
       
    assert response.status_code == 200