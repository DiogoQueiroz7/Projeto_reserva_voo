from datetime import datetime
from typing import Optional
from .airplane import Airplane
from .crewman import Crewman
from .customer import Customer
from .reservation import Reservation
import random 

class Flight:

    '''
    classe que representa um voo 
    '''
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
        '''retorna o código do voo'''
        return self._code
    @property
    def origin(self): 
        '''retorna a origem do voo'''
        return self._origin
    @property
    def destination(self): 
        '''retorna o destino do voo'''
        return self._destination
    @property
    def airplane(self): 
        '''retorna o avião do voo'''
        return self._airplane
    @property
    def departure_time(self): 
        '''retorna a hora de partida do voo'''
        return self._departure_time
    @property
    def reservation(self): 
        '''
        retorna a reserva do voo
        '''
        return self._reservation
    @property
    def crewman(self): 
        '''retorna tripylante do voo'''
        return self._crewman

    def add_crewman(self, crewman: Crewman):
        '''
        adiciona um triupalnte ao voo
        '''
        self._crewman.append(crewman)
        
    def create_reservation(self, customer: Customer, seat: int) -> Optional[Reservation]:
        '''
        cria a reserva
        '''
        if not 1 <= seat <= self._airplane.capacity:
            raise ValueError('O assento não existe')
        if seat in self._reservation:
            raise ValueError('O assento já está ocupado')
        new_reservation = Reservation(customer, seat)
        self._reservation[seat] = new_reservation
        return new_reservation

    def show_passengers(self, quantity: int = 250):
        """Exibe passageiros de maneira aleatório do voo."""
        print(f"\n--- Passageiros do Voo {self.code} ---")    
        if not self._reservation:
            print("Este voo ainda não tem passageiros.")
            return
        all_reservations = list(self._reservation.values())
        random.shuffle(all_reservations)
        show = all_reservations[:quantity]
        for reservation in show:
            print(f"  Assento {reservation.seat}: {reservation.customer.name} (Reserva: {reservation.locator})")
    
    def show_crew(self):
        '''
        função para msotrar a tripulação de voo 
        '''
        print(f"\n--- Tripulação do Voo {self.code} ---")
        if not self._crewman:
            print("Nenhuma tripulação para este voo.")
            return
        for member in self._crewman:
            print(f"  > {member.introduce()}")