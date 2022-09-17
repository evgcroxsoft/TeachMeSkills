# -------------------------------------------------UserServices---------------------------------------------------------------------------------
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.database import get_db
from models.models import User
from security.security import ALGORITHM, get_password_hash, oauth2_scheme, verify_password, SECRET_KEY
from schemas.schemas import UserInScheme


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