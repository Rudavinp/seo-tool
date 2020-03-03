from flask import Flask
from config import Config
from redis import Redis
from rq import Queue
import os
import redis
from worker import conn
import builtins
builtins.unicode = str
from flask_triangle import Triangle

app = Flask(__name__)
Triangle(app)
app.config.from_object(Config)

# r = Redis()
# redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
# conn = redis.from_url(redis_url)
queue = Queue(connection=conn)

from app import routes
#fdsfsdf