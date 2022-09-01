from pydantic import BaseModel


class BaseHost(BaseModel):
    email: str
    name: str


class CreateHost(BaseHost):
    hashed_password: str


class UpdateHost(BaseHost):
    pass


class RetrieveHost(BaseHost):
    id: int

    class Config:
        orm_mode = True
