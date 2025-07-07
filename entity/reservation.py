import string
import random
from .customer import Customer

class Reservation:
    def __init__(self, customer: Customer, seat: int):
        self._customer = customer
        self._seat = seat
        self._locator = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    @property
    def customer(self):
        return self._customer

    @property
    def seat(self):
        return self._seat

    @property
    def locator(self):
        return self._locator

    def __str__(self):
        return f"Reserva {self.locator} - Passageiro: {self.customer.name}, Assento: {self.seat}"