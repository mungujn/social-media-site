from django.conf.urls import url, include

from . import views

app_name = 'Profile'

urlpatterns = [
    url(r'^get_name/', views.get_name, name='get_name'),
    url(r'^get_name/(?P<val>\w)/$', views.get_name, name='get_name'),
]