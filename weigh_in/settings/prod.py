import os
from .common import *


APP_NAME = os.getenv('APP_NAME', 'Weigh-In')
DEBUG = False

WTF_CSRF_SECRET_KEY = 'a random string'

# WTF_CSRF_SECRET_KEY = os.environ.get('WTF_CSRF_SECRET_KEY', 'thisisasecretkey')
SECRET_KEY = os.getenv('SECRET_KEY', 'another secret key')
RECAPTCHA_PUBLIC_KEY = os.getenv('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_PRIVATE_KEY')

if os.environ.get('DATABASE_URL'):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

DEBUG_TB_INTERCEPT_REDIRECTS = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
