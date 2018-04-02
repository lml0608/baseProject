# -*- coding:utf-8 -*-
'''
Created on 2016年9月9日

@author: liubin

'''
import os
from  time import sleep
import unittest
import logging
from appium import webdriver

from testconfig import config

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
APPIUM_LOCAL_HOST_URL = 'http://127.0.0.1:4723/wd/hub'
PLATFORM_VERSION = '8.0.0'

path = "D:\\app\\baseProject\\src\\apk\\TradeSteward.apk"

class testlogin(object):

    # def __init__(self):
    #
    #     self.logger = logging.getLogger(__name__)

    def setUp(self):

        #self.logger.info('.....setup.....')
        desired_caps = {
            'appPackage': 'com.urovo.wugumofang',
            'appActivity': 'com.urovo.activity.login.view.LoginActivity',
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


        sleep(10)


        #self.logger.info('.....start test.....')

        self.driver.find_element_by_id('com.urovo.wugumofang:id/orgIdEdittext').send_keys('0110074')

        sleep(10)

        self.driver.find_element_by_id('com.urovo.wugumofang:id/userNameEditText').send_keys('0532')
        sleep(5)

        self.driver.find_element_by_id('com.urovo.wugumofang:id/passEditText').send_keys('321')
        sleep(5)

        self.driver.find_element_by_id('loginBtn').click()

        sleep(10)




        self.logger.info('.....end test.....')


    def tearDown(self):
        #self.logger.info('.....teardown.....')
        self.driver.quit()



# if __name__ == "__main__":
#
#     unittest.main()


