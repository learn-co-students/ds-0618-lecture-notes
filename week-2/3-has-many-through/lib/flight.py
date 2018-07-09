from lib.query import *
from lib.ticket import Ticket
class Flight:
    _all = []

    def __init__(self, name):
        #the airline that's being initialized add an airline to _all[]
        Flight._all.append(self)
        self._name = name

    @property
    def name(self):
        return self._name

    @classmethod
    def all(cls):
        return cls._all

    def add_airline(self, airline):

        self._airline = airline

    @property
    def airline(self):
        return self._airline

    @classmethod
    def find_by_name(cls, name):
        # go through all of my airlines
        # and find the one that matches by year
        return Query.find_by_name(cls, name)
        # return [object for object in cls.all() if object.name == name]
    
