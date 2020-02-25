from flask import Flask
from config import Config
from redis import Redis
from rq import Queue
import os
app = Flask(__name__)
app.config.from_object(Config)

# r = Redis()
redis_url = os.getenv('REDIST_URL', 'redis://h:pcca8fa4d56999061b8cc40aa6abea4c1fdda75cc3e76e9c7a8f9b5db8ffde17a@ec2-52-2-166-2.compute-1.amazonaws.com:17129')

queue = Queue(connection=redis_url)

from app import routes
