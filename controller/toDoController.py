import connector
from datetime import datetime
import validate.validate as valid
import model.modelResp as im_ModelResp
import config.configLogFile as im_configLogFile
import constant.constant as im_constant

class ToDoController:
    conn = connector.Connector("localhost","root","","todolist")
    modelResp = im_ModelResp.DataResp()
    logController = im_configLogFile.ConfigLogFile().getLogController()
    constant = im_constant.Constant()

    def read_root(self):
        self.logController.genLog({"Hello": "World"},self.logController.info)
        return {"Hello": "World"}

    def read_toDoList(self):
        self.logController.genLog(self.logController.getMsgWithParams(self.constant.startFuction,self.constant.toDoList),self.logController.info)
        validate = valid.Validate()
        sql = """select id,content,DATE_FORMAT(create_dt, '%Y-%m-%d %T') as create_dt,status,
                DATE_FORMAT(status_dt, '%Y-%m-%d %T') as status_dt,
                DATE_FORMAT(finish_dt, '%Y-%m-%d %T') as finish_dt 
                from todolist"""
        
        self.logController.genLog(self.constant.startConnDB,self.logController.info)
        myConn = self.conn.connect_db()
        if(myConn == None):
            resp = validate.checkRespDB(myConn, self.constant.actionSelect)
            self.logController.genLog(str(resp),self.logController.error)
            return resp

        rs = self.conn.read_db(sql,myConn,True)
        resp = rs.to_dict('records')

        self.logController.genLog(self.constant.respWording+str(resp),self.logController.info)
        self.logController.genLog(self.logController.getMsgWithParams(self.constant.endFunction,self.constant.toDoList),self.logController.info)
        return resp


    def read_insertToDo(self,req):
        self.logController.genLog(self.logController.getMsgWithParams(self.constant.startFuction,self.constant.insertToDo),self.logController.info)
        validate = valid.Validate()
        resp = validate.validateInsert(req)
        if(resp != None):
            self.logController.genLog(str(resp),self.logController.error)
            return resp
        
        self.logController.genLog(self.constant.startConnDB,self.logController.info)
        myConn = self.conn.connect_db()
        if(myConn == None):
            resp = validate.checkRespDB(myConn, self.constant.actionSelect)
            self.logController.genLog(str(resp),self.logController.error)
            return resp

        sql = "INSERT INTO todolist(content,create_dt,finish_dt) VALUES (%s,NOW(),%s)"
        val = (str(req.content),req.finish_dt)
        rs = self.conn.queryExecute(sql,myConn,True,val)
        resp = validate.checkRespDB(rs,self.constant.actionInsert)

        self.logController.genLog(self.constant.respWording+str(resp),self.logController.info)
        self.logController.genLog(self.logController.getMsgWithParams(self.constant.endFunction,self.constant.insertToDo),self.logController.info)
        return resp


    def read_editToDo(self,req):
        self.logController.genLog(self.logController.getMsgWithParams(self.constant.startFuction,self.constant.editToDo),self.logController.info)
        validate = valid.Validate()
        resp = validate.validateUpdate(req)
        if(resp != None):
            self.logController.genLog(str(resp),self.logController.error)
            return resp
        
        self.logController.genLog(self.constant.startConnDB,self.logController.info)
        myConn = self.conn.connect_db()
        if(myConn == None):
            resp = validate.checkRespDB(myConn, self.constant.actionSelect)
            self.logController.genLog(str(resp),self.logController.error)
            return resp

        rs = self.findToDoList(req.id,myConn)
        if(rs.to_dict('records') == []):
            resp = self.modelResp.genMsgRespCodeMsg(self.constant.errDB,self.constant.idIsNotFound)
            self.logController.genLog(str(resp),self.logController.error)
            return resp
            
        dataSql = self.genSqlUpdate(req)
        sql = dataSql[0]
        val = tuple(dataSql[1])
        rs = self.conn.queryExecute(sql,myConn,True,val)
        resp = validate.checkRespDB(rs,self.constant.actionUpdate)

        self.logController.genLog(self.constant.respWording+str(resp),self.logController.info)
        self.logController.genLog(self.logController.getMsgWithParams(self.constant.endFunction,self.constant.editToDo),self.logController.info)
        return resp
    

    def read_deleteToDo(self,req):
        self.logController.genLog(self.logController.getMsgWithParams(self.constant.startFuction,self.constant.deleteToDo),self.logController.info)
        validate = valid.Validate()
        resp = validate.validateDelete(req)
        if(resp != None):
            self.logController.genLog(str(resp),self.logController.error)
            return resp
        
        self.logController.genLog(self.constant.startConnDB,self.logController.info)
        myConn = self.conn.connect_db()
        if(myConn == None):
            resp = validate.checkRespDB(myConn, self.constant.actionSelect)
            self.logController.genLog(str(resp),self.logController.error)
            return resp

        rs = self.findToDoList(req.id,myConn)
        if(rs.to_dict('records') == []):
            resp = self.modelResp.genMsgRespCodeMsg(self.constant.errDB,self.constant.idIsNotFound)
            self.logController.genLog(str(resp),self.logController.error)
            return resp

        sql = "DELETE FROM todolist where id = %s"
        val = (req.id,)
        rs = self.conn.queryExecute(sql,myConn,True,val)
        resp = validate.checkRespDB(rs,self.constant.actionDelete)

        self.logController.genLog(self.constant.respWording+str(resp),self.logController.info)
        self.logController.genLog(self.logController.getMsgWithParams(self.constant.endFunction,self.constant.deleteToDo),self.logController.info)
        return resp


    def findToDoList(self,id,myConn):
        self.logController.genLog(self.logController.getMsgWithParams(self.constant.startFuction,self.constant.findToDoList),self.logController.info)
        sql ="Select id,content from todolist where id = "+str(id)
        rs = self.conn.read_db(sql,myConn,False)

        self.logController.genLog(self.constant.respWording+str(rs.to_dict('records')),self.logController.info)
        self.logController.genLog(self.logController.getMsgWithParams(self.constant.endFunction,self.constant.findToDoList),self.logController.info)
        return rs


    def genSqlUpdate(self,req):
        today = None
        params = []
        sql = "Update todolist SET "
        setValue = []
        if(req.status == 1):
            today = datetime.now()

        if(req.content != None):
            setValue.append("content = %s")
            params.append(req.content)
        
        if(req.finish_dt != None):
            setValue.append("finish_dt = %s")
            params.append(req.finish_dt)

        if(req.status != None):
            setValue.append("status = %s")
            setValue.append("status_dt = %s")
            params.append(req.status)
            params.append(today)
        
        if(req.id != None):
            params.append(req.id)

        strValue = ",".join(setValue)
        sql +=  strValue + " where id = %s"

        return [sql,params]