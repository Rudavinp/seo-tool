import time
from rq import Queue
from redis import Redis
import google_app

redis_conn = Redis()
queue = Queue(connection=redis_conn)

job = queue.enqueue(google_app.yandex, ['lol'])
print(job.result)
time.sleep(60)
print(job.result)