"""
Django settings for IamHHB project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tl)&r5*9t8fy(ov_-9-1scj$p%6&giitcd7ua^=3!nh&n-4eyn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if not DEBUG and 'SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = [
    'iamhhb.herokuapp.com',
    'x.graycarl.me',
    'graycarl.me',
    'localhost'
]


# Application definition
INSTALLED_APPS = [
    'webfs.apps.WebfsConfig',
    'blog.apps.BlogConfig',
    'wiki.apps.WikiConfig',
    'pipeline',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'iamhhb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'html', 'templates'),
            os.path.join(BASE_DIR, 'iamhhb', 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': [
                'iamhhb.templatebuiltins'
            ]
        },
    },
]

WSGI_APPLICATION = 'iamhhb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'var', 'db.sqlite3'),
    },
    # 'pg': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'iamhhbdemo',
    #     'USER': 'hongbo',
    #     'HOST': '127.0.0.1',
    #     'PORT': '5432',
    # }
}
# DATABASES['default'] = DATABASES['pg']

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'var', 'statics')
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'html', 'static')
]
# STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
STATICFILES_STORAGE = 'pipeline.storage.NonPackagingPipelineStorage'

# File storage
MEDIA_ROOT = os.path.join(BASE_DIR, 'var', 'fs')
MEDIA_URL = '/fs/'

# Pipeline
PIPELINE = {
    'JAVASCRIPT': {
        'libs': {
            'source_filenames': (
              'libs/jquery/jquery.js',
              'libs/semantic/semantic.js'
            ),
            'output_filename': 'libs.js',
        },
        'site': {
            'source_filenames': (
                'site.js',
            ),
            'output_filename': 'site.js'
        }
    },
    'STYLESHEETS': {
        'libs': {
            'source_filenames': (
                'libs/semantic/semantic.css',
            ),
            'output_filename': 'libs.css'
        },
        'site': {
            'source_filenames': (
                'site.scss',
                'blog/style.scss',
                'wiki/style.scss'
            ),
            'output_filename': 'site.css'
        }
    },
    'COMPILERS': [
        'iamhhb.libs.pipeline.LibSassCompiler'
    ],
    'CSS_COMPRESSOR': 'pipeline.compressors.NoopCompressor',
    'JS_COMPRESSOR': 'pipeline.compressors.NoopCompressor'
}
