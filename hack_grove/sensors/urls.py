from django.conf.urls import url, include, patterns
from . import views
from sensors.views import *

urlpatterns = [url(r'^$', views.turn, name='turn'), ]