from .common import *

DEBUG = False
TESTING = True
WTF_CSRF_ENABLED = False  # Allows form testing
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/privatescale_test'
APP_NAME = 'Testing App Name'