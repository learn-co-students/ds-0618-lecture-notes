from lib.ticket import Ticket

class Passenger:
    _all = []

    def __init__(self, name):
        self._name = name
        Passenger._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def tickets(self):
        return [ticket for ticket in Ticket.all() if ticket.passenger == self]

    @property
    def flights(self):
        [ticket.flight for ticket in self.tickets]
        # tickets
        # for every ticket of the passenger, tell the flight on that ticket

    @classmethod
    def all(cls):
        return cls._all


# Passenger.all()
# homer.flights()
