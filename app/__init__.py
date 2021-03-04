from flask import Flask
from config import Config, DevelopmentConfig
from redis import Redis
from rq import Queue
import os
import redis
from worker import conn

# print(__name__)

def create_app(config_=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(os.environ['APP_SETTINGS'])
    # app.config.from_object(config_)
    # print(app.config)
    # app.config.from_pyfile(config_)
    if app.debug:
        from werkzeug.debug import DebuggedApplication
        app.wsgi_app = DebuggedApplication(app.wsgi_app, True)
    print(app.debug)
    return app

# app = create_app(Config)
# app = Flask(__name__)

# app.config.from_object(DevelopmentConfig)

queue = Queue(connection=conn)
#
# from app import routes
