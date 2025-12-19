"""
Django settings for locationreminder project.
"""

from pathlib import Path
import os

# ----------------------------------------
# BASE DIRECTORY
# ----------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------------------------
# SECURITY
# ----------------------------------------

# 🚨 CHANGE THIS KEY IN PRODUCTION
SECRET_KEY = 'django-insecure-b49wh!6w5ye4jk+158!v7evymx$#26j+rthaq8l^z6v#5%v0gf'

# 🚨 Turn OFF in production
DEBUG = True

ALLOWED_HOSTS = ["*"]   # allow all for local testing


# ----------------------------------------
# INSTALLED APPS
# ----------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # your app
    'reminder',
]


# ----------------------------------------
# MIDDLEWARE
# ----------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'locationreminder.urls'


# ----------------------------------------
# TEMPLATES
# ----------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # important: enable templates folder
        'DIRS': [os.path.join(BASE_DIR, "templates")],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'locationreminder.wsgi.application'


# ----------------------------------------
# DATABASE (using PyMySQL)
# ----------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'locationdb',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


# ----------------------------------------
# PASSWORD VALIDATION
# ----------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]



# ----------------------------------------
# INTERNATIONALIZATION
# ----------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True


# ----------------------------------------
# STATIC FILES
# ----------------------------------------
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")


# ----------------------------------------
# EMAIL SETTINGS (GMAIL SMTP)
# ----------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'kadam5733abhi@gmail.com'
EMAIL_HOST_PASSWORD = 'qnzv eqls agqz yvpr'  # Gmail App Password




# ----------------------------------------
# DEFAULT PRIMARY KEY FIELD TYPE
# ----------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
