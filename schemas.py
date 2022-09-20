import string
from pydantic import BaseModel

class info(BaseModel):
    petName : str
    ownerName : str
    age : int
    type : str
    gender : str