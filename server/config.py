from os import environ
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

config = {
    'APP_ID': environ['FORTIS_APP_ID'],
    'APP_SECRET': environ['FORTIS_APP_SECRET'],
    'REDIRECT_URL': environ['FORTIS_REDIRECT_URL'],
    'AUTH_URL': environ['AUTH_URL'],
}