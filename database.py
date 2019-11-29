from pymongo import MongoClient
import config


def connect():
    host = config.DB_HOST
    port = config.DB_PORT
    database = config.DB_NAME

    url = f'{host}:{port}'
    client = MongoClient(url)
    return client[database]