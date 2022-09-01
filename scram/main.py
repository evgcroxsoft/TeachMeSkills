from fastapi import FastAPI, APIRouter
import uvicorn
from database.database import engine, Base
from routes import hoster
from models import models

# create instance FastAPI
app = FastAPI()
router = APIRouter()


@app.on_event("startup")
async def startup():
    # когда приложение запускается устанавливаем соединение с БД
    pass


@app.on_event("shutdown")
async def shutdown():
    # когда приложение останавливается разрываем соединение с БД
    pass

# create all tables, this line need to be in main.py
Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True)
