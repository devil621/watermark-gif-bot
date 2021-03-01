import os
import requests
import shutil


def download_image(url: str, filename: str) -> bool:
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(filename, 'wb') as file:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, file)
    except Exception as err:
        print(err)
        return False
    else:
        return True


def files(path: str) -> str:
    return os.path.join('files', os.path.basename(path))
