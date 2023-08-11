"""
ASGI config for storefront project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
>>>>>>> a77aecced6d01cf351118df2ea482b17fbe03da9
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings.dev')
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings')
>>>>>>> a77aecced6d01cf351118df2ea482b17fbe03da9

application = get_asgi_application()
