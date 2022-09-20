from sqlalchemy import Column,Integer,String
from database import Base

class info(Base):
    __tablename__='Pet_Information'
    id = Column(Integer,primary_key=True,index=True)
    petName = Column(String)
    ownerName = Column(String)
    age = Column(Integer)
    type = Column(String)
    gender = Column(String)