import requests, zipfile, os

# from download_gdrive import *
import torch


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

if torch.__version__ == '0.4.1':
	file_id = '1gKwE1Ad41TwtAzwDcN3dYa_S6DcVyiSl'
	file_name = 'flownet2_pytorch_041.zip'
else:
	file_id = '1F2h_6e8gyTqxnbmFFW72zsxx_JX0dKFo'	
	file_name = 'flownet2_pytorch_040.zip'

chpt_path = './models/'
if not os.path.isdir(chpt_path):
	os.makedirs(chpt_path)
"""
Donloaded & complied the the snapshot of flownet-2
"""
destination = os.path.join(chpt_path, file_name)
download_file_from_google_drive(file_id, destination) 
unzip_file(destination, chpt_path)
os.system('cd %s/flownet2_pytorch/; bash install.sh; cd ../' % chpt_path)