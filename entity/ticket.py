from .customer import Customer
from .flight import Flight

class Ticket:
    def __init__(self, customer: Customer, flight: Flight, seat: int, locator: str):
        self._customer = customer
        self._flight_code = flight.code
        self._origin = flight.origin
        self._destination = flight.destination
        self._seat = seat
        self._locator = locator
        
    @property
    def customer(self):
        return self._customer

    @property
    def flight_code(self):
        return self._flight_code

    @property
    def origin(self):
        return self._origin

    @property
    def destination(self):
        return self._destination

    @property
    def seat(self):
        return self._seat

    @property
    def locator(self):
        return self._locator

    @seat.setter
    def seat(self, new_seat: int):
        if isinstance(new_seat, int) and new_seat > 0:
            self._seat = new_seat
        else:
            print("ERRO: Número de assento inválido.")
            
    def __str__(self):
        return (f"--- Passagem [Localizador: {self._locator}] ---\n"
                f"    Passageiro: {self._customer.name}\n"
                f"    Voo: {self._flight_code} ({self._origin} -> {self._destination}), Assento: {self._seat}")