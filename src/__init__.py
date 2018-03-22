import logging
import logging.config
import logging.handlers
import time

import os
filepath = os.path.join('D:/app/baseProject/src/conf/evn', 'logging.conf')

print(filepath)

#D:\app\baseProject\conf\evn\logging.conf
#D:\app\baseProject\src\conf\evn\logging.conf

logging.config.fileConfig(filepath)

logger = logging.getLogger(__name__)

curtime = time.strftime("%Y%m%d%H%M%S",time.localtime())

#handler = logging.handlers.TimedRotatingFileHandler(logFile)

fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)-8s: %(message)s'

formatter = logging.Formatter(fmt)


logFile = os.path.abspath(os.path.join(os.getcwd(),'log','log_{}'.format(curtime)))
handler = logging.handlers.RotatingFileHandler(logFile,maxBytes=4096000000,backupCount=9)
handler.setFormatter(formatter)
logger.addHandler(handler)


