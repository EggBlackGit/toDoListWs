from typing import Union
from pydantic import BaseModel

class DataResp(BaseModel):
    respCode: Union[str, None] = None
    respMsg: Union[str, None] = None

    def genMsgResp(self):
        return {"respCode":self.respCode,"msg":self.respMsg}

    def genMsgRespCodeMsg(self,code,msg):
        if(code != None):
            self.respCode = code
        if(msg != None):
            self.respMsg = msg
        return {"respCode":self.respCode,"msg":self.respMsg}