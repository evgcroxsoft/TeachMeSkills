from database.database import SessionLocal

# Database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

