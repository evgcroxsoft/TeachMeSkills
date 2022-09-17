from fastapi import FastAPI
import uvicorn

from endpoints import accommodation, booking, feedback, me, token, searching

# ________________________________________________________MAIN.PY__________________________________________________________________________________

# create instance FastAPI
app = FastAPI(
        version=1,
        title='Dailyrent',
        description='DEVELOPED BY YEVHENII')

app.include_router(token.router, prefix='/api/v1', tags=["Token"])
app.include_router(searching.router, prefix='/api/v1', tags=["Searching"])
app.include_router(me.router, prefix='/api/v1', tags=["User"])
app.include_router(accommodation.router, prefix='/api/v1', tags=["Accommodation"])
app.include_router(booking.router, prefix='/api/v1', tags=["Bookings"])
app.include_router(feedback.router, prefix='/api/v1', tags=["Feedbacks"])


if __name__ == "__main__":
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True)
