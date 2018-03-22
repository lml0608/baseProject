# -*- coding:utf-8 -*-
'''
Created on 2016年9月9日

@author: liubin

'''
import os
from  time import sleep
import unittest

from appium import webdriver

from testconfig import config

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
APPIUM_LOCAL_HOST_URL = 'http://localhost:4723/wd/hub'
PLATFORM_VERSION = '8.0.0'

path = "D:\\app\\com.example.android.apis_1.0.apk"

class TestWebViewAndroid(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'appPackage': 'com.example.android.apis',
            'appActivity': '.view.Animation1',
            'platformName': 'Android',
            'platformVersion': PLATFORM_VERSION,
            'deviceName': '6be7fe3e',
            'app': PATH(path),
            'noReset':'true',
            'unicodeKeyboard':'true',
            'resetKeyboard':'true'
        }
        self.driver = webdriver.Remote(APPIUM_LOCAL_HOST_URL, desired_caps)



    def test_add_contacts(self):

        username = "abc"
        textfields = self.driver.find_element_by_id('com.example.android.apis:id/pw')

        textfields.click
        sleep(10)
        textfields.send_keys(username)

        self.driver.find_element_by_id('com.example.android.apis:id/login').click()


    def tearDown(self):

        self.driver.quit()


if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(TestWebViewAndroid)

    unittest.TextTestRunner(verbosity=2).run(suite)
