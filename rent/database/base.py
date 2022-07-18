import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

POSTGRES_PW = os.environ.get('POSTGRES_PW')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_URL = os.environ.get('POSTGRES_URL')
POSTGRES_DB = os.environ.get('POSTGRES_DB')

SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_URL}/{POSTGRES_DB}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()