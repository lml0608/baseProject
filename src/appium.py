# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
import logging
import time
import os

import subprocess

class appium(object):


    def __init__(self):

        self.logger = logging.getLogger(__name__)


    def start(self):

        self.logger.info('starting Appium Server...')

        currentTime = time.strftime('%Y%m%d%H%M%S',time.localtime())

        udid          = self.getUdid()
        appiumPort    = 1
        bootStrapPort = 2
        seldnroidPort = 3
        chromiumPort  = 4

        logPath       = os.path.abspath(os.path.join(os.getcwd(),'log','AS'+currentTime+'.log'))


        self.process = subprocess.Popen('appium --port={} --bootstrap-port={} --seldnroid-port={} --chromedriver-port={} '
                                        '--log={} -U{}'.format(appiumPort,bootStrapPort,seldnroidPort,chromiumPort,logPath,udid),stdout=subprocess.PIPE,shell=True)



        time.sleep(5)


    def getUdid(self):

        cmd = 'adb devices'

        output = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)

        print(output)

        infoList = output.stdout.read()#split("\r\n") #.strip('List of devices attached')#.split()

        print(str(infoList).split("\\r\\n"))

        for i in str(infoList).split("\\r\\n"):
            print(i)

        x = str(infoList).split("\\r\\n")

        print(x[0])
        print(x[1])
        #x = str(infoList).split("\\r\n").strip('List of devices attached')

        #print(len(x))

        # if infoList != 0:
        #
        #     deviceList = []
        #
        #     for deviceInfo in infoList:
        #
        #         if deviceInfo != 'device':
        #             deviceList.append(deviceInfo)
        #
        #
        # return deviceList[0]


app1 = appium()

app1.getUdid()









