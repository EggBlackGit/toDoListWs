import pathlib
import os
import controller.logController as im_logConTroller

class ConfigLogFile:
    def __init__(self):
        self.pathLogFile = str(pathlib.Path().resolve()) + str(os.sep) +"Log"
        self.namefile = "logFile"
        self.logController = im_logConTroller.LogController("test","toDoListApi",self.pathLogFile,self.namefile)

    def getLogController(self):
        return self.logController