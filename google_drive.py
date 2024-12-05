from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import os

class GoogleDrive:
    SCOPES = ['https://www.googleapis.com/auth/drive.file']

    def __init__(self, creds_file):
        self.creds_file = creds_file
        self.credentials = None

    def login(self):
        if os.path.exists('token.json'):
            self.credentials = Credentials.from_authorized_user_file('token.json', self.SCOPES)
        if not self.credentials or not self.credentials.valid:
            flow = InstalledAppFlow.from_client_secrets_file(self.creds_file, self.SCOPES)
            self.credentials = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(self.credentials.to_json())

    def upload_file(self, file_path, drive_folder_id=None):
        if not self.credentials:
            raise Exception("User not logged in.")
        
        service = build('drive', 'v3', credentials=self.credentials)
        file_metadata = {'name': os.path.basename(file_path)}
        if drive_folder_id:
            file_metadata['parents'] = [drive_folder_id]

        media = MediaFileUpload(file_path, resumable=True)
        uploaded_file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        return uploaded_file['id']
