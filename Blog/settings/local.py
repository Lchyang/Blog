# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

from .common import *

SECRET_KEY = '2pii#c@oh@*gbi@z4r#d8z_(t($*$9uvxh2_99u4fun9oe6cuv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
