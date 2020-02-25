from flask import Flask
from config import Config
# from redis import Redis
# from rq import Queue

app = Flask(__name__)
app.config.from_object(Config)

# r = Redis()
# q = Queue(connection=r)

from app import routes
