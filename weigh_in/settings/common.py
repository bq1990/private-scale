import os

DEBUG = True
WTF_CSRF_SECRET_KEY = 'a random string'
SECRET_KEY = 'another string'
DEBUG_TB_INTERCEPT_REDIRECTS = False
user = os.environ.get('DATA_DB_USER')
password  = os.environ.get('DATA_DB_PASS')
host = os.environ.get('DATA_DB_HOST')
if host:
    SQLALCHEMY_DATABASE_URI = 'postgres://{}:{}@{}/gonano'.format(user, password, host)
else:
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/weigh_in'
SQLALCHEMY_TRACK_MODIFICATIONS = False
APP_NAME = 'Weigh-In'
RECAPTCHA_PUBLIC_KEY = '6Ld-DBEUAAAAAFlREzQd5IWAfyoc2SHlu5yw-LRm'
RECAPTCHA_PRIVATE_KEY = '6Ld-DBEUAAAAACJhGf5DsO6gLuqtxDc6Ed56O03q'