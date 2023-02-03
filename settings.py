DEBUG = False
if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = ['HOST IP', 'DOMAIN NAIM', 'localhost']
...
STATIC_URL = '/static/'
if DEBUG:
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    STATICFILES_DIRS = [
        STATIC_DIR,
        '/var/www/static/',
    ]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )
MEDIA_URL = '/media/'