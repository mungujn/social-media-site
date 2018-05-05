from __future__ import unicode_literals

from django.db import models

# Create your models here.
from Profile.models import Profile


class FriendRequest(models.Model):
    # id is implicit
    to = models.ForeignKey(Profile, on_delete=models.CASCADE) #many friend requests can be sent to one user one relationship
    frm = models.OneToOneField(Profile, on_delete=models.CASCADE) #each friend request originates from one user

    def __str__(self):
        return self.to.username