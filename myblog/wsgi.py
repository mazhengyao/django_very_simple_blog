"""
WSGI config for myblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""
# Python服务器网关接口
# Python应用与Web服务器之间的接口
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')

application = get_wsgi_application()
