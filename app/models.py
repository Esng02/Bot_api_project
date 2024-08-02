from pymongo import MongoClient

# Подключение к базе данных MongoDB
client = MongoClient("mongodb://mongo:27017/")
db = client.messages_db


def get_db():
    """
    Возвращает подключение к базе данных MongoDB
    """
    return db
