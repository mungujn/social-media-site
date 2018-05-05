from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='friends')
    friends = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    bio = models.CharField(max_length=200, blank=True)
    school = models.CharField(max_length=200, blank=True)
    work = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    profile_pic = models.FileField(blank=True) # change to ImageField in prod site to protect against hacks

#TODO: make this optimization after publishing
'''
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
'''