from typing import Union

from fastapi import Depends, FastAPI, HTTPException
from Preferencias import *
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError

fake_user_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}
app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer("/token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated= "auto")

SECRET_KEY = "ce1b3709244deee0d31e2f88ed6dee6f323f09f9785479376425a57c887a22b5"
ALGORITHM = "HS256"

class User(BaseModel):
    username: str
    full_name: Union[str, None] = None
    email: Union[str, None] = None 
    disabled : Union[bool, None] = None

class userInDb(User):
    hashed_password: str

def get_user(db, username):
    if username in db:
        user_list = db[username]
        return userInDb(**user_list)
    return []

def verify_password(plane_password, hashed_password):
    return pwd_context.verify(plane_password, hashed_password)

def authenticate_user(db, username, password):
    user = get_user(db, username)
    if not User:
        raise HTTPException(status_code= 401, detail= "Could not validate credential", headers= 
                            {"WWWW-Authenticate": "Bearer"})
    if not verify_password(password,user.hashed_password):
        raise HTTPException(status_code= 401, detail= "Could not validate credential", headers= 
                            {"WWWW-Authenticate": "Bearer"})
    return user

def create_token(data: dict, time_expire: Union[datetime, None] = None):
    data_copy = data.copy()
    if time_expire is None:
        expires = datetime.utcnow() + timedelta(minutes=15)
    else:
        expires = datetime.utcnow() + time_expire
    data_copy.update({"exp": expires})
    token_jwt = jwt.encode(data_copy, key= SECRET_KEY, algorithm= ALGORITHM)
    return token_jwt

def get_user_current(token: str = Depends(oauth2_scheme)):
    try:
        token_decode = jwt.decode(token, key = SECRET_KEY, algorithms=[ALGORITHM])
        username = token_decode.get("sub")
        if username == None:
            raise HTTPException(status_code= 252, detail= "Error code: 252", headers= 
                            {"WWWW-Authenticate": "Bearer"})
    except JWTError:
        raise HTTPException(status_code= 353, detail= "Error code: 353", headers= 
                            {"WWWW-Authenticate": "Bearer"})
    user = get_user(fake_user_db,username)
    if not user:
        raise HTTPException(status_code= 454, detail= "Error code: 454", headers= 
                            {"WWWW-Authenticate": "Bearer"})
    return user

def get_user_disabled_current(user: User = Depends(get_user_current)):
    if user.disabled:
        HTTPException(status_code= 400, detail= "Inactive User")
    return user

@app.get("/getMensaje/{nombre}")
def read_root(nombre: str):
    return {"Hello": nombre}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/preferencias/{tipo_evento}/{categoria}")
def prefs(tipo_evento,categoria):
    return {imprimir(tipo_evento, categoria)}

@app.get("/users")
def user(user: User = Depends(get_user_disabled_current)):
    return user

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_user_db, form_data.username, form_data.password)
    access_token_expires = timedelta(minutes= 30)
    access_token_jwt = create_token({"sub": user.username}, access_token_expires)
    return {
        "access_token": access_token_jwt,
        "token_type": "bearer"
    }