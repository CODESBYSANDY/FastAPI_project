from fastapi import APIRouter, HTTPException
from app.auth import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

# Dummy user (for learning)
FAKE_USER = {
    "username": "admin",
    "password": "admin123"
}

@router.post("/login")
def login(username: str, password: str):
    if username != FAKE_USER["username"] or password != FAKE_USER["password"]:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": username})
    return {"access_token": token, "token_type": "bearer"}
