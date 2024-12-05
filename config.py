import os

class Config:
    BOT_TOKEN = os.getenv("tk")
    API_ID = int(os.getenv("apiid"))
    API_HASH = os.getenv("apihash")
    AUTHORIZED_USERS = list(map(int, os.getenv("auth").split(',')))
    GDRIVE_CREDENTIALS = os.getenv("gdcred","credentials.json")  # Path to `credentials.json`
    UPLOAD_FOLDER = "uploads/"
