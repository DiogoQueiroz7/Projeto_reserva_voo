from airplane import Airplane
from crewman import Crewman
from customer import Customer
from resrevation import Reservation

class Flight:
    def __init__(self, code: str, orign: str, destiny:str, airplane: Airplane):
        self.code = code
        self.orign = orign
        self.destiny = destiny
        self.airplane = Airplane
        self.reservation = {}
        self.crewman = []
    def add_crewman(self, crewman: Crewman):
        self.crewman.append(crewman) 
        
    def create_reservation(self, customer: Customer, seat:int):
        if not 1<= seat <= self.airplane.capacity: 
            print('Assento Inválido')
            return None
        if seat in self.reservation:
            print('Esse assento já pertence a outra pessoa')
            return None
        