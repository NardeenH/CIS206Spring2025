

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

    def display_info(self):
        return f"Passenger: {self.first_name} {self.last_name}, Email: {self.email}, City: {self.city}, Country: {self.country}"


class VIPPassenger(Passenger):  #  Inheritance
    def __init__(self, first_name, last_name, email, birth_date, address, city, postal_code, country, lounge_access):
        super().__init__(first_name, last_name, email, birth_date, address, city, postal_code, country)
        self.lounge_access = lounge_access  # New attribute

    #New Method
    def upgrade_seat(self):
        return f"{self.first_name} {self.last_name} has been upgraded to First Class!"

    #Overriding display_info()
    def display_info(self):
        base_info = super().display_info()
        lounge = "Yes" if self.lounge_access else "No"
        return f"{base_info}, Lounge Access: {lounge}"

# Demonstration 
vip_passenger = VIPPassenger(
    "Emma", "Watson", "emma.w@email.com", "1992-04-15",
    "321 Elm St", "Chicago", "60616", "USA", True
)

print(vip_passenger.display_info())    
print(vip_passenger.upgrade_seat())   