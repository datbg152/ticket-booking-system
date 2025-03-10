"""
Django settings for ticketing_project project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
import pymysql


pymysql.install_as_MySQLdb()
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-vl1cemz$eltz6fdxogj-2=5-0=iy^e6^f+gi5^w%u#1=j)065u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Use only for testing, not in production!
ALLOWED_HOSTS = ["*"]


# Application definition
#AUTH_USER_MODEL = 'accounts.CustomUser'

INSTALLED_APPS = [
    'accounts',
    'booking',
    'events',
    'payments',
    'paymentapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
]

# Celery Configuration
#local
# CELERY_BROKER_URL = 'redis://localhost:6379/0'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
#image
# CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')
# CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
#aws
CELERY_BROKER_URL = 'redis://clustercfg.myproject-cache.sv0qeo.apn2.cache.amazonaws.com:6379/0'
CELERY_RESULT_BACKEND = 'redis://clustercfg.myproject-cache.sv0qeo.apn2.cache.amazonaws.com:6379/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Seoul'
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_TASK_RESULT_EXPIRES = 86400 
CELERY_IGNORE_RESULT = False

PAYMENT_HOST = 'localhost:8000'
PAYMENT_USES_SSL = False
#PAYMENT_VARIANT_FACTORY = "paymentapp.provider_factory"

PAYMENT_MODEL = 'paymentapp.models.Payment'
PAYMENT_VARIANTS = {
    'default': ('payments.dummy.DummyProvider', {'capture': False})
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ticketing_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'ticketing_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

#Cache
# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.redis.RedisCache",
#         "LOCATION": "redis://localhost:6379/1",  # Database 1
#     }
# }
#considered to add
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": os.getenv('CACHE_LOCATION', 'redis://localhost:6379/1'),
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'mydb',  # Replace with your actual database name
#         'USER': 'root',  # Replace with your MySQL username
#         'PASSWORD': 'mypassword',  # Replace with your MySQL password
#         'HOST': '127.0.0.1',  # Use '127.0.0.1' if needed
#         'PORT': '3306',  # Default MySQL port
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'mydbadmin',
        'PASSWORD': 'ducbg152',
        'HOST': 'myproject-db.cju6mk4sym85.ap-northeast-2.rds.amazonaws.com',
        'PORT': '3306',
    }
}
# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        #"config.authentication.JWTAuthentication",  # 커스텀 JWT 인증 클래스 사용
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SIMPLE_JWT = {
  'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
  
  'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
  
  'ROTATE_REFRESH_TOKENS': False,  
  
  'BLACKLIST_AFTER_ROTATION': True,
  
  'ALGORITHM': 'HS256',
  
  'SIGNING_KEY': SECRET_KEY,
  
  'VERIFYING_KEY': None,  
  'AUTH_HEADER_TYPES': ('Bearer',),
  'USER_ID_FIELD': 'id',  
  'USER_ID_CLAIM': 'user_id',  
  'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),  
  }

