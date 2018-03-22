# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
import logging

class appium(object):


    def __init__(self):

        self.logger = logging.getLogger(__name__)


    def start(self):

        self.logger.info('starting Appium Server...')


