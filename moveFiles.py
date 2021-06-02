from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
drive = GoogleDrive(gauth)

# View all folders and file in your Google Drive
fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()

for file in fileList:
  # Get the folder ID that you want - destination folder
  if file['title'] == 'DestFolder':
      folderId = file['id']
      break
# traverse all the files to move the select files
# below snippet moves all the image files to the destination folder.
for file in fileList:
  if(file['title'].endswith('.JPG')):
    print('Moving:',file['title'])
    file2 = drive.CreateFile({'id':file['id']})
    file2.Upload()
    file2['parents'] = [{"kind": "drive#parentReference", "id": folderId}]
    file2.Upload()
    print('File moved successfully!')
