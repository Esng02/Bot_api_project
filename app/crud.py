def create_message(db, message):
    """
    Сохраняет сообщение в бд.
    - db: подключение к базе данных
    - message: объект сообщения
    """
    db.messages.insert_one(message.dict())


def get_messages(db, skip=0, limit=10):
    """
    Извлекает сообщения из бд с пагинацией.
    - db: подключение к базе данных
    - skip: количество сообщений, которые нужно пропустить
    - limit: максимальное количество сообщений для возврата
    """
    return list(db.messages.find().skip(skip).limit(limit))
