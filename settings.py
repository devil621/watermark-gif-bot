import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')
SESSION_STRING = os.getenv('SESSION_STRING')
WATERMARK = os.getenv(
    'WATERMARK', 'https://user-images.githubusercontent.com/66209958/109513526-35883200-7acb-11eb-97ed-c0b2ca72119a.png')

X_OFF = int(os.getenv('X_OFF', '10'))
Y_OFF = int(os.getenv('Y_OFF', '10'))
