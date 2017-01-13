DEBUG = True
WTF_CSRF_SECRET_KEY = 'a random string'
SECRET_KEY = 'another string'
DEBUG_TB_INTERCEPT_REDIRECTS = False
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/weigh_in'
SQLALCHEMY_TRACK_MODIFICATIONS = False
APP_NAME = 'Weigh-In'
# reCaptcha keys for local use only. Create your own at
# https://www.google.com/recaptcha/intro/
RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'