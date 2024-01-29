"""
Django settings for voiceshare project.
 
Generated by 'django-admin startproject' using Django 4.0.6.
 
For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/
 
For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os 
from pathlib import Path
from .jazmin import JAZZMIN_SETTINGS
 
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
 
 
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/
 
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-72ct@i#m$q9xs(hdhi^^xa5asb!l$81s0+u180-!k^v#+ug=hk'
 
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
 
ALLOWED_HOSTS = [] 
 
# Application definition
 
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'voiceapp'
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
 
ROOT_URLCONF = 'voiceshare.urls'
 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]
 
WSGI_APPLICATION = 'voiceshare.wsgi.application'
 
 
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'voiceapp',
        'HOST':'localhost',
        'USER':'root',
        'PASSWORD':'Olivia837*#&',
        'PORT':'3306'
    }
}
 
 
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
 
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
# https://docs.djangoproject.com/en/4.0/topics/i18n/
 
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'fr'
TIME_ZONE = 'UTC'
 
USE_I18N = True
 
USE_TZ = True
 
 
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
 
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS=[
	# BASE_DIR/'static'
    os.path.join(BASE_DIR, "static"),
    # BASE_DIR/'mystaticfiles'
]

MEDIA_URL='/voice_files/'
MEDIA_ROOT=BASE_DIR/'static'



 
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
 
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = JAZZMIN_SETTINGS
JAZZMIN_SETTINGS["show_ui_builder"] = True
JAZZMIN_SETTINGS["icons"] = { 
    "auth": "fas fa-users-cog",
    "auth.user": "fas fa-user",
    "auth.Group": "fas fa-users",
    "voiceapp.Audio": "fa fa-file-audio",
    "voiceapp.Catagory": "fa fa-th",
    "voiceapp.CollaborateursModel": "fa fa-users",
    "voiceapp.Audio_attribueModel": "fa fa-music",
    "voiceapp.Fichiers_reçusModel": "fa fa-music",
    "voiceapp.User_Voice": "fa fa-share-alt",
    "voiceapp.Audio_User": "fa fa-share-alt",
    "voiceapp.CatagoryModel": "fa fa-th",
}
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-navy",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-purple-moon",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
}

