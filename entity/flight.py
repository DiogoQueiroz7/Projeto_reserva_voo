from datetime import datetime
from typing import Optional
from .airplane import Airplane
from .crewman import Crewman
from .customer import Customer
from .reservation import Reservation

class Flight:
    def __init__(self, code: str, origin: str, destination: str, airplane: Airplane, departure_time: datetime):
        self._code = code
        self._origin = origin
        self._destination = destination
        self._airplane = airplane
        self._departure_time = departure_time
        self._reservation = {}
        self._crewman = []

    @property
    def code(self): 
        return self._code
    @property
    def origin(self): 
        return self._origin
    @property
    def destination(self): 
        return self._destination
    @property
    def airplane(self): 
        return self._airplane
    @property
    def departure_time(self): 
        return self._departure_time
    @property
    def reservation(self): 
        return self._reservation
    @property
    def crewman(self): 
        return self._crewman

    def add_crewman(self, crewman: Crewman):
        self._crewman.append(crewman)
        
    def create_reservation(self, customer: Customer, seat: int) -> Optional[Reservation]:
        if not 1 <= seat <= self._airplane.capacity:
            return None
        if seat in self._reservation:
            return None
        new_reservation = Reservation(customer, seat)
        self._reservation[seat] = new_reservation
        return new_reservation

    def show_passengers(self, quantity: int = 250):
        print(f"\n Lista de Passageiros do Voo {self.code}")
        if not self._reservation:
            print("Este voo ainda não tem passageiros.")
            return
        
        sorted_reservations = sorted(self._reservation.values(), key=lambda r: r.seat)
        
        for i, reservation in enumerate(sorted_reservations):
            if i >= quantity:
                break
            print(f" Assento {reservation.seat}: {reservation.customer.name} (Reserva: {reservation.locator})")

    def show_crew(self):
        print(f"\n--- Tripulação do Voo {self.code} ---")
        if not self._crewman:
            print("Nenhuma tripulação para este voo.")
            return
        for member in self._crewman:
            print(f"  > {member.introduce()}")