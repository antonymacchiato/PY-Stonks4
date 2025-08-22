from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def upload_to_drive(file_path):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()  # Аутентификация через браузер
    drive = GoogleDrive(gauth)
    file = drive.CreateFile({'title': os.path.basename(file_path)})
    file.SetContentFile(file_path)
    file.Upload()
    print(f"File uploaded to Google Drive: {file['title']}")

# Example usage
upload_to_drive("/path/to/file.txt")
