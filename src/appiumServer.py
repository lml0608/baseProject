# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
import logging
import time
import os

import subprocess

from testconfig import config


class appium(object):


    def __init__(self):

        self.logger = logging.getLogger(__name__)


    def start(self):

        self.logger.info('starting Appium Server...')

        currentTime = time.strftime('%Y%m%d%H%M%S',time.localtime())

        #udid          = self.getUdid()
        udid = '6be7fe3e'
        #appiumPort = config['appiumPort']
        #bootStrapPort = config['bootstrapPort']
        #seldnroidPort = config['selendroidPort']
        #chromiumPort = config['chromePort']

        logPath       = os.path.abspath(os.path.join(os.getcwd(),'log','AS'+currentTime+'.log'))
        print(logPath)
        try:

            self.process = subprocess.Popen(
                'appium.cmd --log={}'.format(logPath),
                stdout=subprocess.PIPE, shell=True)

            # self.process = subprocess.Popen('appium.cmd --port={} --bootstrap-port={} --seldnroid-port={} --chromedriver-port={} '
            #                                 '--log={} -U{}'.format(appiumPort,bootStrapPort,seldnroidPort,chromiumPort,logPath,udid),stdout=subprocess.PIPE,shell=True)

        except Exception as e:
            self.logger.error('start appium server failed!')
            self.logger.error('errorMsg:{}'.format(e))
            #os.system('taskkill /im node.exe /f')




        time.sleep(15)


    def stop(self):

        self.logger.info('stop appium server...')
        #self.process.kill()
        os.system('taskkill /im node.exe /f')


#     def getUdid(self):
#
#         cmd = 'adb devices'
#
#         output = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
#
#         print(output)
#
#         infoList = output.stdout.read().strip('List of devices attached').split()
#
#
#         if infoList != 0:
#
#             deviceList = []
#
#             for deviceInfo in infoList:
#
#                 if deviceInfo != 'device':
#                     deviceList.append(deviceInfo)
#
#
#         return deviceList[0]
#
#
# app1 = appium()
#
# #app1.start()
# app1.stop()
# #










