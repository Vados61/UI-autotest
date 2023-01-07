import os

from dotenv import load_dotenv

from utils import dotenv_path

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

APIKEY = os.environ.get('APIKEY')
BASE_URL = os.environ.get('BASE_URL')
