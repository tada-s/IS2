"""
Django settings for srumban project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os, logging

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from scrunban.settings.secret_config import *

# Application definition

PREREQ_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'guardian',
]

PROJECT_APPS = [
    'apps.autenticacion.apps.AutenticacionConfig',
    'apps.administracion.apps.AdministracionConfig',
    'apps.proyecto.apps.ProyectoConfig',
]

INSTALLED_APPS = PREREQ_APPS + PROJECT_APPS


MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'scrunban.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.abspath(os.path.join(BASE_DIR, "../templates/")),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.administracion.context_processors.pending_user_stories_context',
                'apps.administracion.context_processors.pending_notes_context',
                'apps.administracion.context_processors.assignments_context',
                'apps.administracion.context_processors.notifications_count_context',
                'apps.administracion.context_processors.url_names_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'scrunban.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # default
    'guardian.backends.ObjectPermissionBackend',
)


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, "../statics/"))

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.abspath(os.path.join(BASE_DIR, "../static/"))
]

# Logging configuration
LOGGERS_NAME = {
    'proyecto': 'logger_proyecto',
    'administracion': 'logger_administracion',
    'autenticacion': 'logger_autenticacion'
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, '../logs/info.log'),
            'formatter': 'verbose',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        LOGGERS_NAME['proyecto']: {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        LOGGERS_NAME['administracion']: {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        LOGGERS_NAME['autenticacion']: {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        
    },
}

# CONFIGURACIÓN DE LOGIN!!
URL_NAME_FORMAT = '{}_{}'

APP_NAME_AUTENTICACION = 'auth' #TODO NO CAMBIAR!!
APP_NAME_PROJECT = 'project' #TODO NO CAMBIAR!!
APP_NAME_ADM = 'adm' #TODO NO CAMBIAR!!

LOGIN_NAME  = URL_NAME_FORMAT.format( APP_NAME_AUTENTICACION, 'name')
AUTH_NAME   = URL_NAME_FORMAT.format( APP_NAME_AUTENTICACION, 'auth')
DEAUTH_NAME = URL_NAME_FORMAT.format( APP_NAME_AUTENTICACION, 'deauth')

PERFIL_NAME = URL_NAME_FORMAT.format( APP_NAME_AUTENTICACION, 'profile_detail')
PERFIL_PROJECTS = URL_NAME_FORMAT.format( APP_NAME_AUTENTICACION, 'profile_project_list')
PERFIL_EDIT = URL_NAME_FORMAT.format( APP_NAME_AUTENTICACION, 'profile_edit')


PROJECT_ROLE_LIST = URL_NAME_FORMAT.format( APP_NAME_PROJECT, 'role_list')
PROJECT_ROLE_CREATE = URL_NAME_FORMAT.format( APP_NAME_PROJECT, 'role_crud')
PROJECT_ROLE_DELETE = URL_NAME_FORMAT.format( APP_NAME_PROJECT, 'role_delete')
PROJECT_ROLE_DETAIL = URL_NAME_FORMAT.format( APP_NAME_PROJECT, 'role_detail')
PROJECT_ROLE_EDIT = URL_NAME_FORMAT.format( APP_NAME_PROJECT, 'role_edit')
PROJECT_INDEX = URL_NAME_FORMAT.format( APP_NAME_PROJECT, 'role_index')
PROJECT_DEV_LIST = URL_NAME_FORMAT.format( APP_NAME_PROJECT, 'dev_list')
PROJECT_DEV_EDIT = URL_NAME_FORMAT.format( APP_NAME_PROJECT, 'dev_edit')
PROJECT_SPRINT_LIST = URL_NAME_FORMAT.format( APP_NAME_PROJECT, 'sprint_list')
PROJECT_SPRINT_CREATE = URL_NAME_FORMAT.format( APP_NAME_PROJECT, 'sprint_create')
PROJECT_SPRINT_DELETE = URL_NAME_FORMAT.format( APP_NAME_PROJECT, 'sprint_delete')
PROJECT_SPRINT_EDIT = URL_NAME_FORMAT.format( APP_NAME_PROJECT, 'sprint_edit')
PROJECT_SPRINT_DETAIL = URL_NAME_FORMAT.format( APP_NAME_PROJECT, 'sprint_detail')
PROJECT_SPRINT_KANBAN = URL_NAME_FORMAT.format( APP_NAME_PROJECT, 'sprint_kanban')
PROJECT_FLOW_CREATE = URL_NAME_FORMAT.format( APP_NAME_PROJECT, 'flow_create')
PROJECT_FLOW_EDIT = URL_NAME_FORMAT.format( APP_NAME_PROJECT, 'flow_edit')
PROJECT_FLOW_LIST = URL_NAME_FORMAT.format( APP_NAME_PROJECT, 'flow_list')
PROJECT_FLOW_DELETE = URL_NAME_FORMAT.format( APP_NAME_PROJECT, 'flow_delete')
PROJECT_US_DETAIL = URL_NAME_FORMAT.format( APP_NAME_PROJECT, 'us_detail')
PROJECT_US_ADDWORK = URL_NAME_FORMAT.format( APP_NAME_PROJECT, 'us_addwork')
PROJECT_BDC = URL_NAME_FORMAT.format( APP_NAME_PROJECT, 'burndown' )

ADM_PROJECT_LIST = URL_NAME_FORMAT.format( APP_NAME_ADM, 'project_list')
ADM_PROJECT_CREATE = URL_NAME_FORMAT.format( APP_NAME_ADM, 'project_create')
ADM_PROJECT_MODIFY = URL_NAME_FORMAT.format( APP_NAME_ADM, 'project_modify')
ADM_PROJECT_DELETE = URL_NAME_FORMAT.format( APP_NAME_ADM, 'project_delete')
ADM_USER_LIST = URL_NAME_FORMAT.format( APP_NAME_ADM, 'user_list')
ADM_USER_CREATE = URL_NAME_FORMAT.format( APP_NAME_ADM, 'user_create')
ADM_USER_DELETE = URL_NAME_FORMAT.format( APP_NAME_ADM, 'user_delete')
ADM_US_LIST = URL_NAME_FORMAT.format( APP_NAME_ADM, 'userstory_list')
ADM_US_CREATE = URL_NAME_FORMAT.format( APP_NAME_ADM, 'userstory_create')
ADM_US_DELETE = URL_NAME_FORMAT.format( APP_NAME_ADM, 'userstory_delete')
ADM_UST_LIST = URL_NAME_FORMAT.format( APP_NAME_ADM, 'userstorytype_list')
ADM_UST_CREATE = URL_NAME_FORMAT.format( APP_NAME_ADM, 'userstorytype_create')
ADM_UST_DELETE = URL_NAME_FORMAT.format( APP_NAME_ADM, 'userstorytype_delete')
ADM_UST_SUMMARY = URL_NAME_FORMAT.format( APP_NAME_ADM, 'userstorytype_summary')
ADM_FLW_LIST = URL_NAME_FORMAT.format( APP_NAME_ADM, 'flow_list' )
ADM_FLW_CREATE = URL_NAME_FORMAT.format( APP_NAME_ADM, 'flow_create' )
ADM_FLW_DELETE = URL_NAME_FORMAT.format( APP_NAME_ADM, 'flow_delete' )
ADM_FLW_SUMMARY = URL_NAME_FORMAT.format( APP_NAME_ADM, 'flow_summary' )

ADM_NOT_LIST = URL_NAME_FORMAT.format( APP_NAME_ADM, 'notification_list' )

URL_NAMES = {
    'LOGIN_NAME': LOGIN_NAME,
    'AUTH_NAME': AUTH_NAME,
    'DEAUTH_NAME': DEAUTH_NAME,
    'PERFIL_NAME': PERFIL_NAME,
    'PERFIL_PROJECTS': PERFIL_PROJECTS,
    'PERFIL_EDIT': PERFIL_EDIT,
    'PROJECT_ROLE_LIST': PROJECT_ROLE_LIST,
    'PROJECT_ROLE_CREATE': PROJECT_ROLE_CREATE,
    'PROJECT_ROLE_DELETE': PROJECT_ROLE_DELETE,
    'PROJECT_ROLE_DETAIL': PROJECT_ROLE_DETAIL,
    'PROJECT_ROLE_EDIT': PROJECT_ROLE_EDIT,
    'PROJECT_DEV_LIST': PROJECT_DEV_LIST,
    'PROJECT_DEV_EDIT': PROJECT_DEV_EDIT,
    'PROJECT_INDEX': PROJECT_INDEX,
    'PROJECT_SPRINT_LIST': PROJECT_SPRINT_LIST,
    'PROJECT_SPRINT_CREATE': PROJECT_SPRINT_CREATE,
    'PROJECT_SPRINT_DELETE': PROJECT_SPRINT_DELETE,
    'PROJECT_SPRINT_EDIT': PROJECT_SPRINT_EDIT,
    'PROJECT_SPRINT_DETAIL': PROJECT_SPRINT_DETAIL,
    'PROJECT_SPRINT_KANBAN': PROJECT_SPRINT_KANBAN,
    'PROJECT_FLOW_CREATE': PROJECT_FLOW_CREATE,
    'PROJECT_FLOW_EDIT': PROJECT_FLOW_EDIT,
    'PROJECT_FLOW_DELETE': PROJECT_FLOW_DELETE,
    'PROJECT_FLOW_LIST': PROJECT_FLOW_LIST,
    'PROJECT_US_DETAIL': PROJECT_US_DETAIL,
    'PROJECT_US_ADDWORK': PROJECT_US_ADDWORK,
    'PROJECT_BDC': PROJECT_BDC,
    'ADM_USER_LIST': ADM_USER_LIST,
    'ADM_USER_CREATE': ADM_USER_CREATE,
    'ADM_USER_DELETE': ADM_USER_DELETE,
    'ADM_PROJECT_LIST': ADM_PROJECT_LIST,
    'ADM_PROJECT_CREATE': ADM_PROJECT_CREATE,
    'ADM_PROJECT_MODIFY': ADM_PROJECT_MODIFY,
    'ADM_PROJECT_DELETE': ADM_PROJECT_DELETE,
    'ADM_US_LIST': ADM_US_LIST,
    'ADM_US_CREATE': ADM_US_CREATE,
    'ADM_US_DELETE': ADM_US_DELETE,
    'ADM_UST_LIST': ADM_UST_LIST,
    'ADM_UST_CREATE': ADM_UST_CREATE,
    'ADM_UST_DELETE': ADM_UST_DELETE,
    'ADM_UST_SUMMARY': ADM_UST_SUMMARY,
    'ADM_FLW_LIST': ADM_FLW_LIST,
    'ADM_FLW_CREATE': ADM_FLW_CREATE,
    'ADM_FLW_DELETE': ADM_FLW_DELETE,
    'ADM_FLW_SUMMARY': ADM_FLW_SUMMARY,
    'ADM_NOT_LIST': ADM_NOT_LIST,
}


