# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

from src.appiumServer import appium
import logging

logger = logging.getLogger(__name__)

def setUp():

    logger.info('启动Appium Server')
    appium().start()

def tearDown():
    logger.info('关闭Appium Server')
    appium().stop()

