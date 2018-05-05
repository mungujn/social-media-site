from django.conf.urls import url

from django.contrib.auth import views as auth_views
from Home.forms import LoginForm

from . import views

app_name = 'home'

urlpatterns = [
    url(r'login/$', auth_views.login, {'template_name': 'Home/login.html', 'authentication_form': LoginForm},
        name='login'),
    url(r'logout/$', auth_views.logout, {'next_page': '/login'}, name='logout'),
    url(r'^$', views.home, name='home'),
    url(r'contact-us', views.contact, name='contact'),
    url(r'about-us', views.about, name='about'),

]