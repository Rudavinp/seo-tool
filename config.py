import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'lol'
    FLASK_ENV = 'development'
    # PATH = "/usr/local/bin:/usr/bin:/bin:/app/vendor/"
    # LD_LIBRARY_PATH = "/usr/local/lib:/usr/lib:/lib:/app/vendor"
