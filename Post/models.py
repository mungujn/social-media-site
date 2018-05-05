from __future__ import unicode_literals

from django.db import models

# Create your models here.
from Profile.models import Profile


class Post(models.Model):
    #id is implicit
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE) #a user can have many posts
    text = models.CharField(max_length=600)
    image = models.FileField(upload_to='images/posts',blank=True)