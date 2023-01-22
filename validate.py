from datetime import datetime
import model.modelResp as im_ModelResp
import constant.constant as im_constant

class Validate():
    modelResp = im_ModelResp.DataResp()
    constant = im_constant.Constant()
    def validateInsert(self,req):
        if(req.finish_dt != None):
            return self.validateFinish_dt(req.finish_dt)
        return None

    def validateUpdate(self,req):
        count = 0
        if(req.id == None):
            self.modelResp.respCode = self.constant.idIsNoneCode
            self.modelResp.respMsg = self.constant.idIsNoneMsg
            return self.modelResp.genMsgResp()

        if(req.content != None):
            count += 1
        
        if(req.finish_dt != None):
            count += 1
            return self.validateFinish_dt(req.finish_dt)
        
        if(req.status != None):
            count += 1
        
        if(count == 0):
            self.modelResp.respCode = self.constant.leastOneDataCode
            self.modelResp.respMsg = self.constant.leastOneDataMsg
            return self.modelResp.genMsgResp()
        return None
    

    def validateDelete(self,req):
        if(req.id == None):
            self.modelResp.respCode = self.constant.idIsNoneCode
            self.modelResp.respMsg = self.constant.idIsNoneMsg
            return self.modelResp.genMsgResp()
        return None


    def validateFinish_dt(self,finish_dt):
        today = datetime.now()
        chkFormatDT = False

        try:
            datetime.strptime(finish_dt, self.constant.formatDT)
        except Exception:
            chkFormatDT = True
        if(chkFormatDT):
            self.modelResp.respCode = self.constant.incorrectDateFormatCode
            self.modelResp.respMsg = self.constant.incorrectDateFormatMsg
            return self.modelResp.genMsgResp()

        if(finish_dt < str(today)):
            self.modelResp.respCode = self.constant.finishdtMoreTodayCode
            self.modelResp.respMsg = self.constant.finishdtMoreTodayMsg
            return self.modelResp.genMsgResp()

        return None


    def checkRespDB(self,code,flagAction = None):
        if(code == self.constant.successfullyCode):
            self.modelResp.respCode = code
            self.modelResp.respMsg = self.constant.actionSuccessfully % (flagAction)
        elif(code == self.constant.failedCode):
            self.modelResp.respCode = self.constant.errDB
            self.modelResp.respMsg  = self.constant.actionFailed % (flagAction)
        else:
            self.modelResp.respCode = self.constant.errDB
            self.modelResp.respMsg = self.constant.connCantConn
        return self.modelResp.genMsgResp()