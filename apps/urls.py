"""apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
import os

from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse, Http404
from django.conf import settings

import api.urls


def index_html(req):
    """
    Serve index.html with AngularJS app to all requests(like /login, /dashboard, etc.)
    """
    if req.path.startswith('/admin') or req.path.startswith('/api'):
        raise Http404()

    filename = os.path.join(settings.BASE_DIR, 'static', 'index.html')
    with open(filename) as fd:
        return HttpResponse(fd.read())


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(api.urls)),
    url(r'^.*$', index_html, name='index_html')
]
