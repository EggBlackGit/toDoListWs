from typing import Union
from pydantic import BaseModel

class DataReq(BaseModel):
    id: Union[int, None] = None
    content: Union[str, None] = None
    status: Union[bool, None] = None
    finish_dt: Union[str, None] = None