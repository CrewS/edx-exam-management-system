# -*- coding:utf-8 -*-
"""
Django settings for ems project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kd!#xeh^*c4&8y7lc&zp)^c5l)*d241()oj4l7u$u9dhab&7d!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'exam_paper',
]

THIRD_PART_APPS = [
    'rest_framework',
    'social_django',
    'corsheaders',
    'drf_yasg',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PART_APPS


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ems.urls'
LOGIN_URL = 'login/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'build'),
            os.path.join(BASE_DIR, 'ems/build'),
            os.path.join(BASE_DIR, 'exam-frontend/build')
        ],
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

WSGI_APPLICATION = 'ems.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'build/static'),
    os.path.join(BASE_DIR, 'ems/build/static'),
    os.path.join(BASE_DIR, 'exam-frontend/build/static'),
]


# Open edX setttings

EDX_API = {
    'HOST': 'http://0.0.0.0:18010',
    'COURSES': '/exam/courses',
    'COURSE_PROBLEMS': '/exam/problems',
    'COURSE_SECTIONS': '/exam/sections',
    'SECTION_PROBLEMS': '/exam/section/problems',
    'SECTION_PROBLEM_TYPE_COUNT': '/exam/sections/count',
    'PROBLEM_DETAIL': '/exam/problems/detail',
    'PROBLEM_TYPES': '/exam/problem/types',
}

# SSO
AUTHENTICATION_BACKENDS = (
    'auth_backends.backends.EdXOpenIdConnect',
)

EDX_LMS_PATH = ''
SOCIAL_AUTH_EDX_OIDC_KEY = ''
SOCIAL_AUTH_EDX_OIDC_SECRET = ''
SOCIAL_AUTH_EDX_OIDC_URL_ROOT = EDX_LMS_PATH + 'oauth2'
# Identity token decryption key (same value as the client secret for edX OpenID Connect)
SOCIAL_AUTH_EDX_OIDC_ID_TOKEN_DECRYPTION_KEY = ''
SOCIAL_AUTH_EDX_OIDC_ISSUER = EDX_LMS_PATH + 'oauth2'
LOGIN_REDIRECT_URL = '/'

# cross domain
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    '*',
)

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'PATCH',
    'POST',
    'PUT',
)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)

SWAGGER_SETTINGS = {
    'LOGIN_URL': '/login/',
    'LOGOUT_URL': '/logout/',

}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS':
        'exam_paper.pageinations.FormatPageNumberPagination',
    'PAGE_SIZE': 10
}
