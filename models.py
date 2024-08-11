from sqlalchemy import Column, Integer, String, Boolean
from dbconfig import Base

# class Users(Base):
#     __tablename__ = 'users'
    
#     userid = Column(Integer, primary_key = True, index = True, autoincrement = True)
#     username = Column(String(50), unique = True)
#     coins = Column(Integer)

# class Items(Base):
#     __tablename__ = 'items'

#     itemid = Column(Integer, primary_key = True, index = True, autoincrement = True)
#     item_name = Column(String(100))
#     owner = Column(String(50))
#     price = Column(Integer)
#     forsale = Column(Boolean)