from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

testing_obj = {
    "jake": {
        "username": "jake",
        "full_name": "jake",
        "email": "jake@gmail.com",
        "hashed_password": "$2b$12$HxWHkvMuL7WrZad6lcCfluNFj1/Zp63lvP5aUrKlSTYtoFzPXHOtu",
        "disabled": False
    }
}

class User(BaseModel):
	username: str
	email: str or None = None
	full_name: str or None = None
	disabled: bool or None = None

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str or None = None

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()


@app.post("/create/")
async def  create():
	return {}

@app.get("/test/")
async def test():
	return {"hello": "word"}