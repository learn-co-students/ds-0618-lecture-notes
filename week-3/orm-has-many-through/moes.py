from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, ForeignKey, String, Boolean

from sqlalchemy.orm import sessionmaker, relationship, backref
import sqlalchemy

Base = declarative_base()

class Bartender(Base):
    __tablename__ = 'bartenders'
    id = Column(Integer, primary_key = True)
    name = Column(Text)
    hometown = Column(Text)
    birthyear = Column(Integer)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key = True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    bartender_id = Column(Integer, ForeignKey('bartenders.id'))
    drink_id = Column(Integer, ForeignKey('drinks.id'))

class Drink(Base):
    __tablename__ = 'drinks'
    id = Column(Integer, primary_key = True)
    name = Column(Text)
    calories = Column(Text)
    price = Column(Text)
    alcoholic = Column(Boolean)


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key = True)
    name = Column(Text)
    hometown = Column(Text)
    birthyear = Column(Integer)


engine = sqlalchemy.create_engine('sqlite:///moes.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
