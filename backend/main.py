import os
import urllib.parse
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import requests
from dotenv import load_dotenv

load_dotenv()

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")
FRONTEND_URL = os.getenv("FRONTEND_URL")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/auth/login")
def login():
    google_auth_url = "https://accounts.google.com/o/oauth2/v2/auth"
    params = {
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "response_type": "code",
        "scope": "openid profile email",
    }
    url_parse = urllib.parse.urlencode(params)
    return RedirectResponse(f"{google_auth_url}?{url_parse}")

@app.get("/auth/callback")
def auth_callback(code: str = None):
    if not code:
        raise HTTPException(status_code=400, detail="Код авторизации не получен")

    token_url = "https://oauth2.googleapis.com/token"
    token_data = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }

    token_response = requests.post(token_url, data=token_data)
    if token_response.status_code != 200:
        raise HTTPException(status_code=400, detail="Не удалось получить токен от Google")
    
    tokens = token_response.json()
    access_token = tokens.get("access_token")

    userinfo_url = "https://www.googleapis.com/oauth2/v2/userinfo"
    headers = {"Authorization": f"Bearer {access_token}"}
    userinfo_response = requests.get(userinfo_url, headers=headers)
    
    if userinfo_response.status_code != 200:
        raise HTTPException(status_code=400, detail="Не удалось получить данные профиля")

    user_info = userinfo_response.json()
    user_name = user_info.get("name")
    user_avatar = user_info.get("picture")

    encoded_name = urllib.parse.quote(user_name)
    encoded_avatar = urllib.parse.quote(user_avatar)
    
    redirect_target = f"{FRONTEND_URL}/?auth=success&name={encoded_name}&avatar={encoded_avatar}"
    return RedirectResponse(redirect_target)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main.py:app", host="127.0.0.1", port=5000, reload=True)