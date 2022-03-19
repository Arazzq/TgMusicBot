import os
import logging
from dotenv import load_dotenv

if os.path.exists('config.env'):
    load_dotenv('config.env', override=True)


class Config:
    def __init__(self) -> None:
        self.SESSION: str = os.environ.get('SESSION', "1AZWarzsBuzZ5Q4nmQGbtPV_Uv6NypYr7BIz4WglrCICoodUT66pWaqnLKkPAIauD6gLVLMOt4zjf1Db_HvliPaOeMwMs2w3_xi43ZdhNz6B5eaL6yK_euivUbCqC5tED0Q1KCDUW_ul8dvrAXH6H1DpH5ICV4p_SVmt4PLCBtug8TroNK9MofJOFEzi6Ucjlv2hHrSuq5OoHxfCmQhYjjRwfba2qrvIavIoLxqrGbfWaZYq7XwtdffF8pCUGIJOAkOxqOzpIaXFguhWE8cOmWB6fVyYFT0SJOTQghrVqojhnheFl0jidA8M-790s3OjSsNhF4pDjF8JGxpwq5EtTkGdNAcGywcU=")
        self.API_ID: str = os.environ.get('API_ID', "6775827")
        self.API_HASH: str = os.environ.get('API_HASH', "05607067317e01a39ed1e5e1d21dce12") 
        self.SUDO: list = [int(id) for id in os.environ.get(
            'SUDO', ' ').split() if id.isnumeric()]
        if not self.SESSION or not self.API_ID or not self.API_ID:
            print('Error: SESSION, API_ID and API_HASH is required.'
                  'Please check your config.env file.')
            quit(0)
        self.SPOTIFY: bool = False
        self.SPOTIFY_CLIENT_ID: str = os.environ.get('SPOTIFY_CLIENT_ID', None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get(
            'SPOTIFY_CLIENT_SECRET', None)
        _log_level = os.environ.get('LOG_LEVEL', 'error').lower()
        if _log_level == 'error':
            self.LOG_LEVEL = logging.ERROR
        elif _log_level == 'info':
            self.LOG_LEVEL = logging.INFO
        elif _log_level == 'debug':
            self.LOG_LEVEL = logging.DEBUG
        else:
            self.LOG_LEVEL = logging.ERROR
        self.PREFIXES: list = os.environ.get('PREFIX', '!').split()
        self.DEFAULT_LANG: str = os.environ.get('DEFAULT_LANG', 'tr').lower()
        self.DEFAULT_STREAM_MODE: str = 'audio' if (os.environ.get(
            'DEFAULT_STREAM_MODE', 'audio').lower() == 'audio') else 'video'


config = Config()
