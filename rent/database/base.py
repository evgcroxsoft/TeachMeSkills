import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from models import models

# 1.  Get credentials from environments;
POSTGRES_PW = os.environ.get('POSTGRES_PW')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_URL = os.environ.get('POSTGRES_URL')
POSTGRES_DB = os.environ.get('POSTGRES_DB')

# 2. Create path to DB PostgreSQL
SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_URL}/{POSTGRES_DB}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()