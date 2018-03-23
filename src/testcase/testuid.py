# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

from testconfig import config

print(config['appPackage'])
# import subprocess
# import re
#
# cmd = r'adb devices'
# devList = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# devices = []
# for line in devList.stdout.readlines()[1:]:
#     if 'List' not in line:
#         devices.append((line.split('\t'))[0])
# devices.pop()
# print("===devices===")
# print(devices)






#print(str(infoList).split("\\r\\n"))

    # for i in str(infoList).split("\\r\\n"):
    #     print(i)
    #
    # x = str(infoList).split("\\r\\n")
    #
    # print(x[0])
    # print(x[1])
    # x = str(infoList).split("\\r\n").strip('List of devices attached')

    # print(len(x))

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

