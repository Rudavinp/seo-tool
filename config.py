# import os
#
#
# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'lol'
#     FLASK_ENV = 'development'
#     DEBUG = False
#     TESTING = False
#     # PATH = "/usr/local/bin:/usr/bin:/bin:/app/vendor/"
#     # LD_LIBRARY_PATH = "/usr/local/lib:/usr/lib:/lib:/app/vendor"
#
#
# class DevelopmentConfig(Config):
#     DEBUG = True
#
#
# class TestingConfig(Config):
#     TESTING = True

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True