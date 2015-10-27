
from django.conf.urls import include, url

import apps.api.views

urlpatterns = [
    url(r'^$', apps.api.views.home, name='home')
]
