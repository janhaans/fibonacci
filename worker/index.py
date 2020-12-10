import redis
import os

def fib(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fib(num-1) + fib(num-2)

REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
subscription = redis_client.pubsub()
subscription.subscribe('message')

for new_message in subscription.listen():
    redis_client.hset('values', new_message, fib(new_message))