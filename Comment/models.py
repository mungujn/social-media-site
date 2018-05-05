from __future__ import unicode_literals

from django.db import models

# Create your models here.
from Profile.models import Profile


class Comment(models.Model):
    #id is implicit
    post = models.ForeignKey(Profile, on_delete=models.CASCADE) #many comments can be associated with one post
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)#one user per comment
    content = models.CharField(max_length=255)
