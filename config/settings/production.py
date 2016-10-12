# @Author: OUSMANE M. Sadjad <sadjad>
# @Date:   2016-06-27T08:57:50+01:00
# @Email:  ousmanesadjad@gmail.com
# @Last modified by:   sadjad
# @Last modified time: 2016-07-05T11:30:01+01:00



from __future__ import absolute_import

from .common import *


# Allow all host headers
ALLOWED_HOSTS =  ['www.irgibafrica.university', 'irgibafrica.university', 'irgibweb.reysh.com',] #env('ALLOWED_HOSTS')


INSTALLED_APPS +=('gunicorn',)


# EMAIL
# ------------------------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "mail.gandi.net"
EMAIL_HOST_PASSWORD = "4CDLrr000"
EMAIL_HOST_USER = "noreply@irgibafrica.university"
EMAIL_PORT = 465
EMAIL_SUBJECT_PREFIX = "[IRGIB-AFRICA] "
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# LOGGING CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True
        },
        'django.security.DisallowedHost': {
            'level': 'ERROR',
            'handlers': ['console', 'mail_admins'],
            'propagate': True
        }
    }
}
