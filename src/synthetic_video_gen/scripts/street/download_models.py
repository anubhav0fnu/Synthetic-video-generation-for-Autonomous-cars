import os
# Download code taken from Code taken from https://stackoverflow.com questions/25010369/wget-curl-large-file-from-google-drive/39225039#39225039
import requests, zipfile, os
# from scripts.download_gdrive import *

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"
    session = requests.Session()
    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)
    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)
    save_response_content(response, destination)
def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None
def save_response_content(response, destination):
    CHUNK_SIZE = 32768
    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

def unzip_file(file_name, unzip_path):
    zip_ref = zipfile.ZipFile(file_name, 'r')
    zip_ref.extractall(unzip_path)
    zip_ref.close()
    os.remove(file_name)


"""
Merged content from download_gdrive.py

downloads the pre-trained Cityscapes model
"""
file_id = '1MKtImgtnGC28EPU7Nh9DfFpHW6okNVkl'
chpt_path = './checkpoints/'

if not os.path.isdir(chpt_path):
	os.makedirs(chpt_path)

destination = os.path.join(chpt_path, 'models.zip')
download_file_from_google_drive(file_id, destination) 
unzip_file(destination, chpt_path)