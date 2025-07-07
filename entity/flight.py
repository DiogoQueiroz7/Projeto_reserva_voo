from datetime import datetime
from .airplane import Airplane
from .crewman import Crewman
from .customer import Customer
from .reservation import Reservation
from typing import Optional

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
        return self._reservation.copy()

    @property
    def crewman(self):
        return self._crewman.copy()

    @airplane.setter
    def airplane(self, new_airplane: Airplane):
        if isinstance(new_airplane, Airplane):
            self._airplane = new_airplane
        else:
            print("ERRO: O voo precisa de um avião válido.")

    def add_crewman(self, crewman: Crewman):
        self._crewman.append(crewman)
        
    def create_reservation(self, customer: Customer, seat: int) -> Optional[Reservation]:
        if not 1 <= seat <= self._airplane.capacity: 
            print(f"ERRO: O assento {seat} não existe nesse avião.")
            return None
            
        if seat in self._reservation:
            print(f"ERRO: O assento {seat} já está ocupado.")
            return None
            
        new_reservation = Reservation(customer, seat)
        self._reservation[seat] = new_reservation
        return new_reservation

    def make_checkin(self, locator: str) -> Optional['Ticket']:
        from .ticket import Ticket
        found_reservation = None
        for reservation in self._reservation.values():
            if reservation.locator == locator:
                found_reservation = reservation
                break

        if not found_reservation:
            print(f"ERRO: Nenhuma reserva encontrada com o localizador '{locator}'.")
            return None
        
        was_successful = found_reservation.make_checkin()

        if was_successful:
            ticket = Ticket(found_reservation.customer, self, found_reservation.seat, found_reservation.locator)
            return ticket
        
        print("Falha no check-in. A reserva pode já ter sido utilizada ou cancelada.")
        return None

    def show_passengers(self, quantity: int = 10):
        print(f"\n Lista de Passageiros do Voo {self.code} (amostra de {quantity})")
        
        if not self._reservation:
            print("Este voo ainda não tem passageiros.")
            return
            
        sorted_reservations = sorted(self._reservation.values(), key=lambda r: r.seat)
        
        for i, reservation in enumerate(sorted_reservations):
            if i >= quantity:
                break
            print(f" Assento {reservation.seat}: {reservation.customer.name} (Reserva: {reservation.locator})")