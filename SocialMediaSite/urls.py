"""SocialMediaSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
admin user = nickson
admin password = 12345678nineten
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from Home import views

urlpatterns = [
    url(r'profile/', include('Profile.urls')),
    url(r'home/', include('Home.urls')),
    url(r'posts/', include('Post.urls')),
    url(r'comments/', include('Comment.urls')),
    url(r'friends/', include('Friend.urls')),
    url(r'admin/', admin.site.urls),
    url(r'script/', include('script.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
