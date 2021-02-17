#creating tables for database
from sqlalchemy import Boolean,Column,ForeignKey,Integer,String,Numeric,Date
from sqlalchemy.orm import relationship
from database import Base


class Expense(Base):
    __tablename__ = 'expense'

    id = Column(Integer,primary_key =True, index=True)
    date= Column(Date)
    description = Column(String(15)) #max is 15 characters
    currency = Column(String(3)) #max is 3 characters
    amount = Column(Numeric(10,2),index=True)

