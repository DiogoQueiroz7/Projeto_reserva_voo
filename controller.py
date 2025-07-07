from faker import Faker
from datetime import date, datetime
from entity.airplane import Airplane
from entity.flight import Flight
from entity.customer import Customer
from entity.crewman import Crewman
from typing import Optional

class FlightOperator:
    def __init__(self, name: str):
        self._name = name
        self._fleet = []
        self._flights = {}
        self.faker = Faker('pt_BR')
        self._initialize()

    @property
    def name(self):
        return self._name
    
    @property
    def fleet(self):
        return self._fleet
    
    @property
    def flights(self):
        return self._flights

    @name.setter
    def name(self, new_name: str): 
        if isinstance(new_name, str) and len(new_name) > 2:
            self._name = new_name
        else: 
            print('ERRO: Nome da Companhia Inválido.')

    def add_airplane_to_fleet(self, airplane: Airplane):
        if isinstance(airplane, Airplane):
            self._fleet.append(airplane)
        else: 
            print('ERRO: Apenas aviões podem ser adicionados à frota.')

    def schedule_flight(self, flight: Flight):
        if isinstance(flight, Flight):
            self._flights[flight.code] = flight
        else:
            print('ERRO: Apenas voos podem ser agendados.')

    def find_flight(self, code: str) -> Optional[Flight]:
        return self._flights.get(code)

    def _initialize(self):
        self.add_airplane_to_fleet(Airplane("Boeing", "777", "PR-BJB", 250))
        self.add_airplane_to_fleet(Airplane("Airbus", "A380", "AB-STJ", 250))
        self.add_airplane_to_fleet(Airplane("Boeing", "747", "DQ-DQS", 250))

        data_flights = [
            {"codigo": "LA-3100", "origem": "São Paulo (GRU)", "destino": "Salvador (SSA)", "horario": datetime(2025, 11, 10, 9, 0)},
            {"codigo": "LA-3102", "origem": "Rio de Janeiro (GIG)", "destino": "Fortaleza (FOR)", "horario": datetime(2025, 11, 10, 10, 30)},
            {"codigo": "G3-1400", "origem": "Belo Horizonte (CNF)", "destino": "Recife (REC)", "horario": datetime(2025, 11, 11, 7, 15)},
            {"codigo": "G3-1404", "origem": "Brasília (BSB)", "destino": "Manaus (MAO)", "horario": datetime(2025, 11, 11, 14, 0)},
            {"codigo": "AD-2010", "origem": "Campinas (VCP)", "destino": "Porto Alegre (POA)", "horario": datetime(2025, 11, 12, 20, 0)},
            {"codigo": "AD-2012", "origem": "Curitiba (CWB)", "destino": "Natal (NAT)", "horario": datetime(2025, 11, 12, 21, 45)},
            {"codigo": "TP-0082", "origem": "Lisboa (LIS)", "destino": "São Paulo (GRU)", "horario": datetime(2025, 11, 13, 11, 0)},
            {"codigo": "TP-0084", "origem": "Porto (OPO)", "destino": "Rio de Janeiro (GIG)", "horario": datetime(2025, 11, 13, 12, 30)},
            {"codigo": "IB-6025", "origem": "Madrid (MAD)", "destino": "Salvador (SSA)", "horario": datetime(2025, 11, 14, 16, 0)},
            {"codigo": "IB-6027", "origem": "Barcelona (BCN)", "destino": "Fortaleza (FOR)", "horario": datetime(2025, 11, 14, 18, 20)}
        ]

        for i, flight_data in enumerate(data_flights):
            airplane_select = self._fleet[i % len(self._fleet)]

            flight = Flight(
                code=flight_data["codigo"],
                origin=flight_data["origem"],
                destination=flight_data["destino"],
                airplane=airplane_select,
                departure_time=flight_data["horario"]
            )
            
            self.schedule_flight(flight)

            for number_seat in range(1, flight.airplane.capacity + 1):
                customer = Customer(
                    name=self.faker.name(),
                    cpf=self.faker.cpf(),
                    date_of_birth=self.faker.date_of_birth(minimum_age=1, maximum_age=105),
                    email=self.faker.email()
                )
                
                flight.create_reservation(customer, number_seat)

        print(f"Simulação inicializada com {len(self._flights)} voos totalmente preenchidos.")
        print("-" * 30)