from environment import *

twa = Airline(1980, 'twa')
delta = Airline(1992, 'delta')
fivefortyfive = Flight('fivefortyfive')
fivefortyfive.add_airline(twa)
sixfortysix = Flight('sixfortysix')
sixfortysix.add_airline(twa)
sivesixtyseven = Flight('sivesixtyseven')
sivesixtyseven.add_airline(delta)


# single source of truth
# Twa(flight)
#     flight.airline = self

flight1
    'name' | twa

flight2
    'name' | delta


twa

delta



flight1.add_airline(twa)


category has many foods

fruit

vegetable



food belongs to a food category
    carrot
        vegetable
    apple
        fruit
