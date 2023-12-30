from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str or None = None
    full_name: str or None = None
    disabled: bool or None = None
    
app = FastAPI()

@app.post("/create/")
async def  create():
  return {}

@app.get("/test/")
async def test():
  return {"hello": "word"}