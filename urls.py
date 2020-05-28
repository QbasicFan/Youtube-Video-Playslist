#urls.py
from django.conf.urls import url
from . import views


urlpatterns = [
#test this !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    url(r'', views.ytpList, name='ytpList'),

    ]
