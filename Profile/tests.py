import os
import time

from django.conf import settings
from django.test import TestCase, override_settings, Client

from controller import ProfileInterface, checkIfUsernameExists

# Create your tests here.
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


def getTestUserDetails():
    return {
        'username': 'nickson',
        'password': 'password',
        'email': 'example@example.com',
        'first_name': 'Mungujakisa',
        'last_name': 'Nickson',
        'bio': 'The mind once enlightened cannot again become dark',
        'school': 'Makerere',
        'work': 'Looking',
        'location': 'Kampala'
    }


def createTestUserProfile(details):
    interface = ProfileInterface()
    interface.createUserProfile(details)


class ProfileTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.interface = ProfileInterface()
        cls.test_user_details = getTestUserDetails()
        cls.interface.createUserProfile(cls.test_user_details)

    def test_createUserProfile(self):
        createTestUserProfile(getTestUserDetails())
        self.assertEqual(True, True)

    def test_addPictureToProfile(self):
        test_file = open(os.path.join("test_profile_pic.jpg"), "r", 0)
        test_file_contents = test_file.read()

        self.interface.addPictureToProfile(test_file.name, test_file_contents)

        profile = self.interface.getBoundProfile()
        uploaded_file = open(os.path.join("media", profile.user.username + os.path.sep +  "test_profile_pic.jpg"), "r", 0)
        uploaded_file_contents = uploaded_file.read()

        self.assertEqual(test_file_contents, uploaded_file_contents)

        test_file.close()
        uploaded_file.close()

    def test_usernameExists(self):
        self.assertEqual(False, checkIfUsernameExists('mungujakisa'))
        self.assertEqual(True, checkIfUsernameExists(self.test_user_details['username']))


class TestProfileInteraction(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super(TestProfileInteraction, cls).setUpClass()
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super(TestProfileInteraction, cls).tearDownClass()

    @override_settings(DEBUG=True)
    def test_viewOwnProfile(self):
        profile_details = getTestUserDetails()
        createTestUserProfile(profile_details)
        self.login(profile_details)
        self.driver.get('%s%s' % (self.live_server_url, '/profile/view/' + profile_details['username']))
        profile_button_text = self.getTextInElementWithID("id_button")
        self.assertEqual(profile_button_text, "Edit Profile")
        self.assertEqual(self.driver.title, "nickson")

    @override_settings(DEBUG=True)
    def test_createProfile(self):
        self.driver.get('%s%s' % (self.live_server_url, '/profile/create-profile'))
        try:
            self.fillInRegistrationForm()
            self.assertEqual(self.driver.title, "Create Profile")
            self.driver.find_element_by_id('submit_button').submit()
            self.holdPageOpen()
        except Exception, arg:
            print arg
            self.fail()

    def fillInRegistrationForm(self):
        details = getTestUserDetails()
        self.sendInputToElement('id_first_name', details['first_name'])
        self.sendInputToElement('id_last_name', details['last_name'])
        self.sendInputToElement('id_username', details['username'])
        self.sendInputToElement('id_password', details['password'])
        self.sendInputToElement('id_bio', details['bio'])
        self.sendInputToElement('id_school', details['school'])
        self.sendInputToElement('id_work', details['work'])
        self.sendInputToElement('id_location', details['location'])
        self.sendInputToElement('id_email', details['email'])
        profile_picture = self.driver.find_element_by_id("picture")  # TODO google how to do uploads with selenium

    def sendInputToElement(self, element_id, input):
        element = self.driver.find_element_by_id(element_id)
        element.send_keys(input)

    def holdPageOpen(self):
        wait_in_seconds = 30
        time.sleep(wait_in_seconds)

    def waitForInputBeforeQuiting(self):
        str = input("Enter anything to quit")

    def login(self, details):
        self.driver.get('%s%s' % (self.live_server_url, '/login'))
        self.sendInputToElement("id_username", details['username'])
        self.sendInputToElement("id_password", details['password'])
        self.driver.find_element_by_id('id_username').submit()

    def loginProgrammatically(self, details):
        client = Client()
        client.login(username=details['username'], password=details['password'])
        cookie = client.cookies['sessionid']
        self.driver.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
        self.driver.get('%s%s' % (self.live_server_url, '/home'))

    def getTextInElementWithID(self, element_id):
        return self.driver.find_element_by_id(element_id).text


