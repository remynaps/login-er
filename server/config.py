from os import environ
from os.path import join, dirname

config = {
    'APP_ID': environ['FORTIS_APP_ID'],
    'APP_SECRET': environ['FORTIS_APP_SECRET'],
    'REDIRECT_URL': environ['FORTIS_REDIRECT_URL'],
    'AUTH_URL': environ['AUTH_URL'],
}