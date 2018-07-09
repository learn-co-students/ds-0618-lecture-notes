from lib.query import *
from lib.flight import *

class Airline:
    _all = []

    def __init__(self, year, name):
        #the airline that's being initialized add an airline to _all[]
        Airline._all.append(self)
        self._year = year
        self._name = name

    @property
    def year(self):
        return self._year
    # year = property(year)

    @property
    def name(self):
        return self._name
    # name = property(name)

    @name.setter
    def name(self, name):
        self._name = name

    @year.setter
    def year(self, year):
        self._year = year

    # year = year.setter(year)
    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def find_by_year(cls, year):
        # go through all of my airlines
        # and find the one that matches by year
        return [airline for airline in cls.all() if airline.year == year]

    @classmethod
    def find_by_name(cls, name):
        # go through all of my airlines
        # and find the one that matches by year
        return Query.find_by_name(cls, name)

    # flight -> airline
    #
    # what we want:
    # airline -> flights
    def flights(self):
        return [flight for flight in Flight.all() if flight.airline == self ]
        # go through all the instances of flights
        # and answer the question is the airline equal to the airline who is receiving the method call
