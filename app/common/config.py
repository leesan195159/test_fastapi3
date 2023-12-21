from dataclasses import dataclass
from os import path, environ

import configparser
from fastapi import Request

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))

# async def get_header(http_host: str = Header(None))


@dataclass
class Config:
    BASE_DIR = base_dir


@dataclass
class LocalConfig(Config):
    config = configparser.ConfigParser()
    config.read('/home/sara/PycharmProjects/pythonProject/app/database/config.ini')
    # environ["API_ENV"] = "local"
    DB_URL: str = config.get('develop', 'host').strip("'")
    DB_USER: str = config.get('develop', 'user').strip("'")
    DB_PASSWORD: str = config.get('develop', 'password').strip("'")
    DB: str = config.get('develop', 'database').strip("'")


@dataclass
class ProdConfig(Config):
    PROJ_RELOAD: bool = False


def conf():
    config = dict(prod=ProdConfig, local=LocalConfig)
    return config[environ.get("API_ENV", "local")]()
