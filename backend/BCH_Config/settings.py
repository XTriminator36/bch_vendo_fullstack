"""
Django settings for BCH_Config project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path
from datetime import timedelta


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-==yik&*#(gm+6fi(#n&a^%^&32uszyqi5hl!%e)_y)x#bgklk('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#SESSIONS FOR AUTH
#auto logout function
AUTO_LOGOUT ={
    'IDLE_TIME': timedelta(hours=3), #Idling session is set to 3 Hours
    'SESSION_TIME': timedelta(hours=8), #Total session time is 8 Hours
    'REDIRECT_TO_LOGIN_IMMEDIATELY': True,
    'MESSAGE': 'Idling for too long, Please re-login again',
}



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #django rest framework
    'rest_framework',
    'corsheaders',

    #install necessary apps
    'Main',
    'api', 

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django_auto_logout.middleware.auto_logout', #django auto logout middleware
    'Main.middleware.AdminRedirectMiddleware',
]

ROOT_URLCONF = 'BCH_Config.urls'

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

                'django_auto_logout.context_processors.auto_logout_client', #auto logout template
            ],
        },
    },
]

WSGI_APPLICATION = 'BCH_Config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

#Configure your db here
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Vendo_DB',
        'USER': 'postgres',
        'PASSWORD': 'ninjaxvd',
        'HOST': 'localhost', # Change locale if other specified
        'PORT': '9341',  # Change the port number here if other port specified
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

# <-- ALLOWED URLS FOR CORS (DRF DEPLOYMENT) -->

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_HEADERS = "access-control-allow-origin" , "Content-Type"
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8080", #allowed url for getting the apis
    "http://127.0.0.1   :5173"
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR / 'Main/media/')
MEDIA_URL = '/Main/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/Main/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#Celery Broker (remove this comment when docking/deploying)
#CELERY_BROKER_URL = 'redis://localhost:6379'

# google account needed
#GOOGLE_MAPS_API_KEY = 'your_api_key_here'

