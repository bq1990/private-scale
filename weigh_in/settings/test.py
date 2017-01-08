from .common import *

DEBUG = False
TESTING = True
WTF_CSRF_ENABLED = False  # Allows form testing
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/weigh_in_test'
APP_NAME = 'Testing App Name'