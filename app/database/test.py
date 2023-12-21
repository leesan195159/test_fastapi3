import configparser
import os
from os import environ

from fastapi import Request


config = configparser.ConfigParser()
config.read('config.ini')
print(config.get('develop', 'host'))
environ["DB_URL"] = config.get('develop', 'host')
for key, value in os.environ.items():
    print(f'{key}: {value}')
# print(config.get(['develop']))