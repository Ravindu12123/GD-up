from pyrogram import Client, filters
from pyrogram.types import Message
import os
from google_drive import GoogleDrive
from config import Config

app = Client("drive_bot", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN)
drive_accounts = {}

# Authorize users only
@app.on_message(filters.command("start") & filters.user(Config.AUTHORIZED_USERS))
async def start(client, message: Message):
    await message.reply("Welcome! Use /login to connect Google Drive and /upload to upload files.")

@app.on_message(filters.command("login") & filters.user(Config.AUTHORIZED_USERS))
async def login(client, message: Message):
    user_id = message.from_user.id
    drive = GoogleDrive(Config.GDRIVE_CREDENTIALS)
    drive.login()
    drive_accounts[user_id] = drive
    await message.reply("Google Drive account connected successfully!")

@app.on_message(filters.command("upload") & filters.user(Config.AUTHORIZED_USERS))
async def upload(client, message: Message):
    user_id = message.from_user.id
    if user_id not in drive_accounts:
        await message.reply("Please use /login first.")
        return
    
    if not message.reply_to_message or not message.reply_to_message.document:
        await message.reply("Reply to a document to upload.")
        return

    document = message.reply_to_message.document
    file_path = await message.reply_to_message.download(Config.UPLOAD_FOLDER + document.file_name)
    drive = drive_accounts[user_id]
    
    try:
        uploaded_file_id = drive.upload_file(file_path)
        await message.reply(f"File uploaded successfully! File ID: {uploaded_file_id}")
        os.remove(file_path)  # Clean up after upload
    except Exception as e:
        await message.reply(f"Upload failed: {str(e)}")
