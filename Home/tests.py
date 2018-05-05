
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
# Create your tests here.


class SeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(SeleniumTests, cls).setUpClass()
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super(SeleniumTests, cls).tearDownClass()

    def test_createProfile(self):
        self.driver.get('%s%s' % (self.live_server_url, '/login/'))


    def test_login(self):
        self.driver.get('%s%s' % (self.live_server_url, '/login/'))
        username_input = self.driver.find_element_by_name("username")
        password_input = self.driver.find_element_by_name("password")
        username_input.send_keys('myuser')
        password_input.send_keys('secret')
        self.driver.find_element_by_xpath('//input[@value="Register"]').click()