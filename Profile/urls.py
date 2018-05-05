from django.conf.urls import url

from . import views

app_name = 'profile'

urlpatterns = [
    url(r'^create-profile/$', views.createProfileView, name='register'),
    url(r'^view/(?P<username>\w+)/$', views.viewProfile, name='profile'),  # usernames are case sensitive
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^all/$', views.all, name='all'),
    url(r'^add-friend/$', views.addFriend, name='add-friend'),
]
