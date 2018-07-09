1. Domain modeling
2. Where is the data stored
3. Difference between underlying data and the query


1. Now we want to build out a passenger class
  a passenger has a name, which is  
2. Also build out a ticket class
  Consider the data that should be stored on each instance of a ticket
3. Consider where the relationship between a passenger and a ticket
 - write a method to call `ticket.passenger` which returns the passenger associated with a ticket
 - write a method to call `passenger.tickets` to return the list of tickets associated with each passenger
4. Write a method called `flight.tickets` to return the list of all `tickets` associated with a flight
5. Write a method called `flight.passengers` to return a list of the passengers associated


Where to start, and workflow
1. Relationships




Ticket
  belongs to passenger
  belongs to flight
  belongs to airline

Passenger
  has many flights
  has many tickets
  has many tickets

Airline
  has many tickets
  has many flights
  has many passengers

Flight
  belongs to airline
  has many tickets
  has many passengers

Tickets
  |12| marge| # 765|  
  |12| lisa | # 766|  
  |12| bart | # 765|  
  |12| homer | # 456|

Go through all of the tickets associated with marget
And then finding that flight
[ticket.flight for ticket in marge.tickets]
