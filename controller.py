from faker import Faker
from datetime import date, datetime
from typing import Optional
from entity.airplane import Airplane
from entity.flight import Flight
from entity.customer import Customer
from entity.crewman import Crewman

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
            print('ERRO: Apenas Aviões podem ser adicionados à frota.')
    
    def schedule_flight(self, flight: Flight):
        if isinstance(flight, Flight):
            self._flights[flight.code] = flight
        else:
            print('ERRO: Apenas voos podem ser agendados.')

    def find_flight(self, code: str) -> Optional[Flight]:
        return self._flights.get(code)

    def _initialize(self):

        print("Loading...")

        self.add_airplane_to_fleet(Airplane(model="777", fabricator="Boeing", register="PR-BJB", capacity=250))
        self.add_airplane_to_fleet(Airplane(model="A380", fabricator="Airbus", register="AB-STJ", capacity=250))
        self.add_airplane_to_fleet(Airplane(model="747", fabricator="Boeing", register="DQ-DQS", capacity=250))
        print(f"Frota criada com {len(self._fleet)} aeronaves.")
        
        crew_team_A = [
            Crewman("Carlos Souza", "111.111.111-11", date(1985, 5, 20), "carlos.s@airline.com", "Piloto", "pass1"),
            Crewman("Ana Pereira", "222.222.222-22", date(1990, 3, 15), "ana.p@airline.com", "Copiloto", "pass2"),
            Crewman("João Silva", "333.333.333-33", date(1982, 12, 1), "joao.s@airline.com", "Comissário", "pass3")
        ]
        crew_team_B = [
            Crewman("Roberto Lima", "444.444.444-44", date(1988, 7, 30), "roberto.l@airline.com", "Piloto", "pass4"),
            Crewman("Mariana Alves", "555.555.555-55", date(1991, 9, 5), "mariana.a@airline.com", "Copiloto", "pass5"),
            Crewman("Fernanda Costa", "666.666.666-66", date(1987, 11, 10), "fernanda.c@airline.com", "Comissário", "pass6")
        ]
        crew_teams = [crew_team_A, crew_team_B]

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
            
            assigned_team = crew_teams[i % len(crew_teams)]
            for member in assigned_team:
                flight.add_crewman(member)
            
            self.schedule_flight(flight)

            for number_seat in range(1, flight.airplane.capacity + 1):
                customer = Customer(
                    name=self.faker.name(),
                    cpf=self.faker.cpf(),
                    date_of_birth=self.faker.date_of_birth(minimum_age=1, maximum_age=105),
                    email=self.faker.email()
                )
                flight.create_reservation(customer, number_seat)

        print(f"Loading... {len(self._flights)} voos criados e populados.")
        print("-" * 30)