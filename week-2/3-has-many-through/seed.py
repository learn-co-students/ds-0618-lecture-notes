from environment import *

twa = Airline(1980, 'twa')
delta = Airline(1992, 'delta')

fivefortyfive = Flight('fivefortyfive')
sixfortysix = Flight('sixfortysix')
sivesixtyseven = Flight('sivesixtyseven')

fivefortyfive.add_airline(twa)
sixfortysix.add_airline(twa)
sivesixtyseven.add_airline(delta)

marge = Passenger('marge')
lisa = Passenger('lisa')
homer = Passenger('homer')

ticket_one = Ticket(marge, sixfortysix)
ticket_two = Ticket(homer, sixfortysix)
ticket_three = Ticket(homer, fivefortyfive)
ticket_four = Ticket(lisa, fivefortyfive)
