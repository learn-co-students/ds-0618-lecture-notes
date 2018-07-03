class Airline:

    _all = []

    def __init__(self, year):
        print(vars(self))
        #the airline that's being initialized add an airline to _all[]
        Airline._all.append(self)
        self._year = year

    @property
    def year(self):
        return self._year
    # year = property(year)

    @year.setter
    def year(self, year):
        self._year = year

    def foobar(self):
        return 'foobar'
    # year = year.setter(year)
    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def find_by_year(cls, year):
        # go through all of my airlines
        # and find the one that matches by year
        return [airline for airline in cls.all() if airline.year == year]

    # all = classmethod(all)
    # @year.deletr
    # def year(self):
    #     del self._year
    # year.deletr(year)


# query
    # reading
# command
    # create
    # update
    # delete
