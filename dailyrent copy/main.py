from fastapi import FastAPI
import uvicorn
from endpoints import accommodation, booking, feedback, me, searching

# ________________________________________________________MAIN.PY__________________________________________________________________________________

# create instance FastAPI
app = FastAPI()
v1 = FastAPI()
app.mount("/api/v1", v1)


if __name__ == "__main__":
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True)
