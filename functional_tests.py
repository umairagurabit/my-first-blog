from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
import time
import unittest

class BlogOverallTest(unittest.TestCase):

    def setUp(self):
        caps = DesiredCapabilities.FIREFOX

        caps["binary"] = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"

        geckodriver = r'C:\Users\kevin\myweb\geckodriver-v0.26.0-win64\geckodriver.exe'

        self.browser = webdriver.Firefox(capabilities=caps, executable_path=geckodriver)

    def tearDown(self):

        self.browser.quit()

    def test_login(self):
        self.browser.get('http://localhost:8000/accounts/login/')
        # user opens web browser, navigates to admin page
        #self.browser.get(self.live_server_url + '/accounts/login/')
        # users types in username and passwords and presses enter
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('Test')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('123testing123')
        password_field.send_keys(Keys.RETURN)
        # login credentials are correct, and the user is redirected to the main admin page
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn("Welcome to Minchang's blog", body.text)
        time.sleep(2)

    def test_add_newPost(self):
        self.browser.get('http://localhost:8000/post/new')
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('Test')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('123testing123')
        password_field.send_keys(Keys.RETURN)
        #body = self.browser.find_element_by_tag_name('body')
        #self.assertIn("Welcome to Minchang's blog", body.text)
        self.browser.find_element_by_name('title').send_keys('Testing')
        self.browser.find_element_by_id('id_text').send_keys("test success")
        time.sleep(1)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
