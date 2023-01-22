import mysql.connector 
import pandas as pd
import config.configLogFile as im_configLogFile
import constant.constant as im_constant

class Connector:
    logController = im_configLogFile.ConfigLogFile().getLogController()
    constant = im_constant.Constant()
    def __init__(self,host,user,password,database) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database = database


    def connect_db(self):
        mydb = None
        try:
            mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
            )
            self.logController.genLog(self.constant.connSuccessfully,self.logController.info)
        except mysql.connector.Error as err:
            print(err)
        return mydb

        
    def queryExecute(self,sql,conn,closeConn,param=None):
        try:
            rs = None
            if(conn.is_connected()):
                mycursor = conn.cursor()
                self.logController.genLog(self.constant.sqlWording+str(sql),self.logController.info)
                self.logController.genLog(self.constant.paramsWording+str(param),self.logController.info)
                if(param == None):
                    mycursor.execute(sql)
                else:
                    mycursor.execute(sql,param)
                conn.commit()
                mycursor.close()
                rs = self.constant.successfullyCode
            else:
                self.logController.genLog(self.constant.connCantConn,self.logController.info)
                print(self.constant.connCantConn)
        except Exception as err:
            rs = self.constant.failedCode
            print(self.constant.executeFailed)
            print(err)
            self.logController.genLog(self.constant.exceptionWording+str(err),self.logController.error)
        finally:
            if(closeConn != False and conn.is_connected()):
                conn.close()
                self.logController.genLog(self.constant.connClose,self.logController.info)
                print(self.constant.connClose)
        return rs


    def read_db(self,sql,conn,closeConn):
        try:
            rs = None
            if(conn.is_connected()):
                mycursor = conn.cursor()
                self.logController.genLog(self.constant.sqlWording+str(sql),self.logController.info)
                rs = pd.read_sql(sql,conn)
                mycursor.close()
            else:
                self.logController.genLog(self.constant.connCantConn,self.logController.info)
                print(self.constant.connCantConn)
        except Exception as err:
            print(self.constant.readFailed)
            print(err)
            self.logController.genLog(self.constant.exceptionWording+str(err),self.logController.error)
        finally:
            if(closeConn!=False and conn.is_connected()):
                conn.close()
                self.logController.genLog(self.constant.connClose,self.logController.info)
                print(self.constant.connClose)
        return rs
