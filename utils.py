import os
import requests
import shutil


def download_image(url: str, filename: str) -> bool:
    os.makedirs('files',exist_ok=True)
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            print('Got file response')
            with open(filename, 'wb') as file:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, file)
    except Exception as err:
        print(err)
        return False
    else:
        print('File created image')
        return True


def files(path: str) -> str:
    return os.path.join('files', os.path.basename(path))
