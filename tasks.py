import time
from rq import Queue
from redis import Redis
from google_app import yandex

redis_conn = Redis()
queue = Queue(connection=redis_conn)

job = queue.enqueue(yandex, ['lol'])
print(job.result)
time.sleep(60)
print(job.result)