from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY='django-insecure-7_*jfrb9r+ki5jb#xmz%14a7k8@7-*q-$1qfd=5nr09tph28)7'
DEBUG=True

ALLOWED_HOSTS = [
    '*'
]

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
    'tailwind',
    'theme',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    "crispy_tailwind",
    'core',
    'accounts',
    'social',
]

SITE_ID = 1

TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = [
    "127.0.0.1",
]

NPM_BIN_PATH = 'C:/Program Files/nodejs/npm.cmd'

CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]
# ================ ALLAUTH ==================== #
ACCOUNT_ALLOW_REGISTRATION = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_UNIQUE = True
AUTH_USER_MODEL = "accounts.User"
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "account_login"
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = None
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/'

ACCOUNT_RATE_LIMITS = {
    "login": "5/m",  
    "login_failed": "5/m",  
    "signup": "5/m",  
    "password_reset": "3/m" 
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware'
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# DATABASES = {
#     "default": env.db("DATABASE_URL", default="postgres:///social"),
# }
# DATABASES["default"]["ATOMIC_REQUESTS"] = True

DATABASES  = {
    "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
}


PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'

if not DEBUG:
    EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'EMAIL_HOST'
    EMAIL_HOST_USER = 'EMAIL_HOST_USER'
    EMAIL_HOST_PASSWORD = 'EMAIL_HOST_PASSWORD'
    EMAIL_PORT = 'EMAIL_PORT'
    EMAIL_USE_TLS = 'EMAIL_USE_TLS'
    SESSION_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_REDIRECT_EXEMPT = []
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # django-ckeditor will not work with S3 through django-storages without this line in settings.py
    AWS_QUERYSTRING_AUTH = False

    # aws settings

    AWS_ACCESS_KEY_ID = 'AWS_ACCESS_KEY_ID'
    AWS_SECRET_ACCESS_KEY = 'AWS_SECRET_ACCESS_KEY'
    AWS_STORAGE_BUCKET_NAME = 'AWS_STORAGE_BUCKET_NAME'


    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    AWS_DEFAULT_ACL = 'public-read'

    # s3 static settings

    STATIC_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    # s3 public media settings

    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'core.storage_backends.MediaStore'

    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')