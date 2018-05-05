# In the clean architecture approach, this is the controller/interface
import os
from abc import ABCMeta, abstractmethod

from django.contrib.auth.models import User
from django.core.files.base import ContentFile

from Profile.models import Profile
from SocialMediaSite import settings


class ServerInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def createUserProfile(self, details):
        pass

    @abstractmethod
    def addPictureToProfile(self, filename, picture):
        pass

    @abstractmethod
    def getProfileWithUsername(self, username):
        pass


def getFriends():
    return None


def createUserObject(details):
    user = User.objects.create_user(
        details['username'],
        details['email'],
        details['password']
    )
    user.first_name = details['first_name']
    user.last_name = details['last_name']
    return user


def saveUser(user_object):
    user_object.save()


def createProfileObject(user, details):
    profile = Profile.objects.create(
        user=user,
        bio=details['bio'],
        school=details['school'],
        work=details['work'],
        location=details['location']
    )
    return profile


def saveProfile(profile_object):
    profile_object.save()


def getProfile(username):
    try:
        profile = Profile.objects.get(user__username=username)
        return profile
    except Profile.DoesNotExist:
        return None


def checkIfUsernameExists(username):
    try:
        user = User.objects.get(username=username) #TODO lookup a better technique
        return True
    except:
        return False


class ProfileInterface(ServerInterface):

    def getProfileWithUsername(self, username):
        return getProfile(username)

    def __init__(self):
        self.profile = None

    def createUserProfile(self, details):
        user = createUserObject(details)
        self.profile = createProfileObject(user, details)
        saveProfile(self.profile)

    def addPictureToProfile(self, filename, picture):
        if self.checkIfFileExists(filename):
            self.deleteFile(filename)

        server_name = self.__getCleanFilename(filename)
        self.profile.profile_pic.save(server_name, ContentFile(picture))

    def getBoundProfile(self):
        return self.profile


    def checkIfFileExists(self, filename):
        path = os.path.join(settings.MEDIA_ROOT, self.__getCleanFilename(filename))
        return os.path.exists(path)

    def deleteFile(self, filename):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.__getCleanFilename(filename)))
        pass

    def __getCleanFilename(self, filename):
        directory = self.profile.user.username
        name = directory + os.path.sep + filename
        return name

