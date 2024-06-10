import requests 
from flask import current_app


def get_file(file_id):
    response = requests.post(
        
        current_app.config['FILE_SERVER_URL'],
        json={'file_id': file_id},
        verify=current_app.config['FILE_SERVER_CERT_PATH']
    )
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()