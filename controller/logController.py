import logging
from datetime import datetime
import os

class LogController:
    debug = "debug"
    info ="info"
    warning = "warning"
    error = "error"
    
    def __init__(self, text="", app="", path_log_app="", namefile=""):
        self.app_name = app
        self.text_long = text
        self.logger = logging.getLogger(app)
        self.logger.setLevel(logging.DEBUG)
        self.path_log_app = path_log_app
        self.namefile = namefile
        
    def genLog(self, message, level):
        if not os.path.exists(self.path_log_app):
            os.makedirs(self.path_log_app)
        file_name = self.path_log_app + str(os.sep) + self.namefile + datetime.now().strftime("%Y_%m_%d")+ ".log"
        fh = logging.FileHandler(file_name, encoding = "UTF-8")
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        if(level == self.debug):
            self.logger.debug(message)
        elif(level == self.info):
            self.logger.info(message)
        elif(level == self.warning):
            self.logger.warning(message)
        elif(level == self.error):
            self.logger.error(message)
        else:
            self.logger.critical(message)
        self.logger.handlers.clear()
        return True

    def getMsgWithParams(self,constant,msgreplace):
        return constant % (msgreplace)