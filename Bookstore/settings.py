"""
Django settings for Bookstore project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import environ
import django_heroku
from pathlib import Path
from decouple import config
import os

env=environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 
SECRET_KEY = config("DJANGO_SECRET_KEY",default='django-insecure-+*@pchsapa@$taympvh^a6ro5-31lg+j6b18ytjvbq_jwbg+my')
# print(SECRET_KEY, "\n")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DJANGO_DEBUG",default=True, cast=bool)
# print(DEBUG,"\n")
ALLOWED_HOSTS = ['forscholars.herokuapp.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_social_share',

    #local apps
    'mainapp.apps.MainappConfig',
    'accounts.apps.AccountsConfig',

    #3rd aprty apps
    'django_extensions',
    "crispy_forms",
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'Bookstore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR /'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'mainapp.context_processors.ads',
          
            ],
        },
    },
]

WSGI_APPLICATION = 'Bookstore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

# Authentication 
AUTH_USER_MODEL="accounts.CustomUser"

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
# AWS_ACCESS_KEY_ID= 
# AWS_SECRET_ACCESS_KEY= 
# AWS_STORAGE_BUCKET_NAME='forscholarsbucket'
# AWS_S3_CUSTOM_DOMAIN='%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# AWS_S3_OBJECT_PARAMETERS={'CacheControl':'max-age=86400'}
# AWS_DEFAULT_ACL='public-read'

# AWS_LOCATION='static'



STATICFILES_DIRS =[os.path.join(BASE_DIR, 'static'),]
STATIC_ROOT = os.path.join(BASE_DIR / "staticfiles")
STATIC_URL='/static'
MEDIA_URL='/media/'
MEDIA_ROOT= os.path.join( BASE_DIR/'media/')
CRISPY_TEMPLATE_PACK='bootstrap4'

django_heroku.settings(locals())
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT=425
EMAIL_USE_TLS=True
EMAIL_HOST_USER='nwaforglory6@gmail.com'
EMAIL_HOST_PASSWORD='qjkcabzjrvxqpxsa'
print(EMAIL_HOST_PASSWORD, '....')


# AWS_ACCESS_KEY=config('AWS_ACCESS_KEY')
# AWS_SECRET_KEY=config('AWS_SECRET_KEY')
# AWS_STORAGE_BUCKET_NAME='forscholars'
# AWS_S3_FILE_OVERWRITE=False
# AWS_DEFAULT_ACL=None
# AWS_DEFAULT_ACL='public-read'
# AWS_S3_CUSTOM_DOMAIN='%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# DEFAULT_FILE_STORAGE='storages.backends.s3boto3.S3Boto3Storage'
# print(AWS_SECRET_KEY,'set')