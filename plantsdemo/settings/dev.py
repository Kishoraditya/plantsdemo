from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-jm&%^!__0$0-!+b!njnlo#+^v#juo^g%)34+3@5##difu4kf_o"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
#from .base import *
#from home.firebase import get_firebase_app

# Other settings...

#get_firebase_app()