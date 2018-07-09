class Ticket:
    _all = []
    def __init__(self, passenger, flight):
        self._passenger = passenger
        self._flight = flight
        Ticket._all.append(self)


    @classmethod
    def all(cls):
        return cls._all

    @property
    def passenger(self):
        return self._passenger

    @property
    def flight(self):
        return self._flight


#ticket =  Ticket(bart, sivesixtyseven)
# ticket.flight.airline
