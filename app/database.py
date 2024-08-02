import redis

redis_client = redis.Redis(host='redis', port=6379, db=0)


def cache_messages(messages):
    redis_client.set('messages', messages)


def get_cached_messages():
    return redis_client.get('messages')
