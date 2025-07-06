import string
import random
from .customer import Customer
from .status import StatusReservation

class Reservation:
    def __init__(self, customer: Customer, seat: int):
        self._customer = customer
        self._seat = seat
        self._status = StatusReservation.CONFIRMADA
        self._locator = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    @property
    def customer(self):
        return self._customer

    @property
    def seat(self):
        return self._seat

    @property
    def status(self):
        return self._status

    @property
    def locator(self):
        return self._locator

    @seat.setter
    def seat(self, new_seat: int):
        if isinstance(new_seat, int) and new_seat > 0:
            self._seat = new_seat
        else:
            print("ERRO: Número de assento inválido.")

    def make_checkin(self) -> bool:
        if self._status == StatusReservation.CONFIRMADA:
            self._status = StatusReservation.CHECKIN_REALIZADO
            print(f"Check-in realizado para a reserva {self._locator}.")
            return True
        print(f"ERRO: Check-in não pôde ser realizado (Status atual: {self._status.name}).")
        return False

    def cancel(self):
        if self._status != StatusReservation.CANCELADA:
            self._status = StatusReservation.CANCELADA
            print(f"Reserva {self._locator} foi cancelada.")