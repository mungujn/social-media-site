from django.conf.urls import url

from . import views

app_name = 'Post'

urlpatterns = [
    url(r'all', views.posts, name='posts'),
    url(r'post', views.post, name='posts'),
]