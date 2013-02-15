import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

# ADMINS = frozenset(['youremail@yourdomain.com'])
SECRET_KEY = 'Album_Session___SIGN___Corea'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'album.db')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8

CSRF_ENABLED = True
CSRF_SESSION_KEY = 'CSRF_SESSION_KEY_ALBUM___SIGN___Corea'

# RECAPTCHA_USE_SSL = False
# RECAPTCHA_PUBLIC_KEY = 'blahblahblahblahblahblahblahblahblah'
# RECAPTCHA_PRIVATE_KEY = 'blahblahblahblahblahblahprivate'
# RECAPTCHA_OPTIONS = {'theme': 'white'}
