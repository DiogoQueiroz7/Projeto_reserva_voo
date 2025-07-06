from .airplane import Airplane
from .crewman import Crewman
from .customer import Customer
from .reservation import Reservation

class Flight:
    def __init__(self, code: str, origin: str, destination: str, airplane: Airplane):
        self._code = code
        self._origin = origin
        self._destination = destination
        self._airplane = airplane
        self._reservations = {}
        self._crew = []

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
    def reservations(self):
        return self._reservations.copy()

    @property
    def crew(self):
        return self._crew.copy()

    @code.setter
    def code(self, new_code: str):
        if isinstance(new_code, str) and len(new_code) > 3:
            self._code = new_code
        else:
            print("ERRO: Código de voo inválido.")

    @airplane.setter
    def airplane(self, new_airplane: Airplane):
        if isinstance(new_airplane, Airplane):
            self._airplane = new_airplane
        else:
            print("ERRO: Avião inválido.")

    def add_crew_member(self, crew_member: Crewman):
        self._crew.append(crew_member)
        
    def create_reservation(self, customer: Customer, seat: int) -> Reservation | None:
        if not 1 <= seat <= self._airplane.capacity: 
            print(f"ERRO: Assento {seat} é inválido (Capacidade: {self._airplane.capacity}).")
            return None
            
        if seat in self._reservations:
            print(f"ERRO: Assento {seat} já está ocupado.")
            return None
            
        new_reservation = Reservation(customer, seat)
        self._reservations[seat] = new_reservation   
        return new_reservation