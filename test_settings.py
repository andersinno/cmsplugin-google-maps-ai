import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
assert os.path.isfile(os.path.join(BASE_DIR, 'manage.py'))

DEBUG = True
VAR_ROOT = os.path.join(BASE_DIR, 'var')
SECRET_KEY = 'really_secret'

if not os.path.isdir(VAR_ROOT):
    print('Creating var root %s' % VAR_ROOT)
    os.makedirs(VAR_ROOT)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_db',
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'cms',
    'menus',
    'treebeard',
    'cmsplugin_google_maps_ai',
]

LANGUAGES = [
    ("en-us", "English"),
]

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
            ],
        },
    },
]

ROOT_URLCONF = 'urls'
SITE_ID = 1
STATIC_ROOT = os.path.join(VAR_ROOT, 'static')
MEDIA_ROOT = os.path.join(VAR_ROOT, 'media')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
WSGI_APPLICATION = 'test_wsgi.application'
