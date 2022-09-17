# ________________________________________________________SECURITY__________________________________________________________________________________
from base64 import b64encode
from datetime import datetime, timedelta
from jose import jwt
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from secrets import token_bytes

from fastapi import APIRouter
router = APIRouter(tags=["Token"])



# -------------------------------------------------Hashing and Verify Password---------------------------------------------------------------------------------


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


async def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# -------------------------------------------------Oauth2---------------------------------------------------------------------------------

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/token")

# -------------------------------------------------JWT Token---------------------------------------------------------------------------------

SECRET_KEY = b64encode(token_bytes(32)).decode()
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


async def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt