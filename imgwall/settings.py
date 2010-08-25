try:
    from djangoappengine.settings_base import *
    has_djangoappengine = True
except ImportError:
    has_djangoappengine = False
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG

import os

SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc433((7yd0dbrakhvi';
DEFAULT_CHARSET = 'utf-8';
INSTALLED_APPS = (
    'djangotoolbox',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
	'imgboards',
    'gaebar',
    'ragendja',
)
LOGIN_REDIRECT_URL = '/'

# Change the User model and admin classes
AUTH_USER_MODULE = 'ragendja.auth.google_models'
AUTH_ADMIN_MODULE = 'ragendja.auth.google_admin'
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'ragendja.auth.middleware.GoogleAuthenticationMiddleware',

)
TEMPLATE_CONTEXT_PROCESSORS = ( 
    'django.core.context_processors.auth', 
    'django.core.context_processors.request'
) 



if has_djangoappengine:
    INSTALLED_APPS = ('djangoappengine',) + INSTALLED_APPS

TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'

ADMIN_MEDIA_PREFIX = '/media/admin/'
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

ROOT_URLCONF = 'urls'

GAEBAR_LOCAL_URL = 'http://localhost:8000'
GAEBAR_SECRET_KEY = '@#d$kdjifik*&32jkjf'
GAEBAR_SERVERS = {
    u'Deployment': u'i-oo-i.appspot.com', 
    u'Staging': u'http://i-oo-i.appspot.com', 
    u'Local Test': u'http://localhost:8000',
}

GAEBAR_MODELS = (
     (
          'imgboards.models', 
          (u'ImgParseConfig', u'ImgLinkPage'),
     ),
)
