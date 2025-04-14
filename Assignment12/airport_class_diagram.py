
class Person:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

class Passenger(Person):
    def __init__(self, first_name, last_name, email, birth_date, address, city, postal_code, country):
        super().__init__(first_name, last_name, email)
        self.birth_date = birth_date
        self.address = address
        self.city = city
        self.postal_code = postal_code
        self.country = country

class TransportEntity:
    def __init__(self, departure_time, arrival_time):
        self.departure_time = departure_time
        self.arrival_time = arrival_time

class Flight(TransportEntity):
    def __init__(self, flight_id, flight_number, airline, terminal, departure_airport, arrival_airport, departure_time, arrival_time):
        super().__init__(departure_time, arrival_time)
        self.flight_id = flight_id
        self.flight_number = flight_number
        self.airline = airline
        self.terminal = terminal
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport

class Airline:
    def __init__(self, airline_id, name):
        self.airline_id = airline_id
        self.name = name

class Airport:
    def __init__(self, airport_id, name, city, country):
        self.airport_id = airport_id
        self.name = name
        self.city = city
        self.country = country

class Terminal:
    def __init__(self, terminal_id, number_of_gates):
        self.terminal_id = terminal_id
        self.number_of_gates = number_of_gates

class Booking:
    def __init__(self, booking_id, passenger, flight, booking_date, price):
        self.booking_id = booking_id
        self.passenger = passenger
        self.flight = flight
        self.booking_date = booking_date
        self.price = price

# Multiple Inheritance Example
class PassengerDetails:
    def __init__(self, passenger):
        self.passenger = passenger

class BoardingInfo:
    def __init__(self, boarding_time, seat):
        self.boarding_time = boarding_time
        self.seat = seat

class BoardingPass(PassengerDetails, BoardingInfo):
    def __init__(self, boarding_id, passenger, flight, boarding_time, seat):
        PassengerDetails.__init__(self, passenger)
        BoardingInfo.__init__(self, boarding_time, seat)
        self.boarding_id = boarding_id
        self.flight = flight

class Baggage:
    def __init__(self, baggage_id, boarding_pass):
        self.baggage_id = baggage_id
        self.boarding_pass = boarding_pass
