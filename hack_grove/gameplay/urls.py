from django.conf.urls import url, include, patterns
from . import views
from gameplay.views import *

urlpatterns = [url(r'^$', views.index, name='index'), ]
