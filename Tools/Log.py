import logging
from Settings import ApiSettings
import os

class Log(object):
    @staticmethod
    def getLog(name):
        logger = logging.getLogger(name)
        if not os.path.isdir(ApiSettings.LOG_DIR):
            os.mkdir(ApiSettings.LOG_DIR)
        logAddress = "%s/%s.log"%(ApiSettings.LOG_DIR,name)
        handler = logging.FileHandler(logAddress)
        formatter = logging.Formatter(ApiSettings.FORMAT)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        return logger