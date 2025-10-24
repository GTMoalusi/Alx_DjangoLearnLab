# social_media_api/settings.py

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# (Security and Debug settings would be here)
SECRET_KEY = 'django-insecure-your-secret-key' # Placeholder, replace with actual key
DEBUG = True
ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',
    'rest_framework.authtoken', # REQUIRED: Enables Token Authentication models

    # Local apps (MUST be added)
    'accounts.apps.AccountsConfig', 
    'posts',
]

# (MIDDLEWARE, ROOT_URLCONF, TEMPLATES, DATABASES, etc. remain the same)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'social_media_api.urls'

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

WSGI_APPLICATION = 'social_media_api.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# (Password validation, Internationalization, Static files settings remain the same)

# --- Custom API/Auth Settings ---

# MANDATORY: Set the custom User model defined in accounts/models.py
AUTH_USER_MODEL = 'accounts.User' 

# Django REST Framework Settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # Use Token authentication as the primary method
        'rest_framework.authentication.TokenAuthentication', 
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        # Default to requiring authentication unless explicitly overridden
        'rest_framework.permissions.IsAuthenticated', 
    )
}

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
