from sqlalchemy import Column, Integer, Text, String, DateTime
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Apartment(Base):
    __tablename__ = 'apartments'
    id = Column(Integer, primary_key = True)
    title = Column(Text)
    price = Column(Integer)
    date = Column(DateTime)
    neighborhood = Column(Text)
