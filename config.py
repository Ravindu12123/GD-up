import os

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    API_ID = int(os.getenv("API_ID"))
    API_HASH = os.getenv("API_HASH")
    AUTHORIZED_USERS = list(map(int, os.getenv("AUTHORIZED_USERS").split(',')))
    GDRIVE_CREDENTIALS = os.getenv("GDRIVE_CREDENTIALS")  # Path to `credentials.json`
    UPLOAD_FOLDER = "uploads/"
