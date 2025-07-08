from faker import Faker
from datetime import date, datetime
from typing import Optional
from entity.airplane import Airplane
from entity.flight import Flight
from entity.customer import Customer
from entity.crewman import Crewman
import time
class FlightOperator:
    '''
    classe principal do sistema, gerencia todo o programa... popula, cria e inicia
    '''
    def __init__(self, name: str):
        self.name = name
        self._fleet = []
        self._flights = {}
        self.faker = Faker('pt_BR')
        self._initialize()

    @property
    def name(self):
        '''retorna o nome da companhia'''
        return self._name
    
    @property
    def fleet(self):
        '''retorna a frota'''
        return self._fleet
    
    @property
    def flights(self):
        '''retorna os voos o dicionario de voos'''
        return self._flights
        
    @name.setter
    def name(self, new_name: str): 
        '''
        valida o nome da comapahia do programa, se tiver menos de 2 letras, levanta erro
        '''
        if isinstance(new_name, str) and len(new_name) > 2:
            self._name = new_name
        else: 
            raise ValueError("ERRO: Nome da Companhia Inválido. Deve ter mais de 2 caracteres.")

    def add_airplane_to_fleet(self, airplane: Airplane):
        '''adicona um avião a frota'''
        if isinstance(airplane, Airplane):
            self._fleet.append(airplane)
        else: 
            raise TypeError('ERRO: Apenas Aviões podem ser adicionados à frota.')
    
    def schedule_flight(self, flight: Flight):
        '''verifica se um voo é valido para introduzir ele na biblioteca de voos'''
        if isinstance(flight, Flight):
            self._flights[flight.code] = flight
        else:
            raise TypeError('ERRO: Apenas voos podem ser agendados.')

    def find_flight(self, code: str) -> Optional[Flight]:
        '''
        busca um voo agendado pelo seu código 
        '''
        return self._flights.get(code)

    def _initialize(self):
        print("Entrando no Sistema do IFMS Airlines Group ")
        time.sleep(2)

        self.add_airplane_to_fleet(Airplane(model="777", fabricator="Boeing", register="PR-BJB", capacity=250))
        self.add_airplane_to_fleet(Airplane(model="A380", fabricator="Airbus", register="AB-STJ", capacity=250))
        self.add_airplane_to_fleet(Airplane(model="747", fabricator="Boeing", register="DQ-DQS", capacity=250))
        print(f"IFMS Airlines Group possui {len(self._fleet)} aeronaves.")
        time.sleep(2)
        
        crew_team_A = [
            Crewman("Carlos Souza", "111.111.111-11", date(1985, 5, 20), "carlos.s@airline.com", "Piloto"),
            Crewman("Ana Pereira", "222.222.222-22", date(1990, 3, 15), "ana.p@airline.com", "Copiloto"),
            Crewman("João Silva", "333.333.333-33", date(1982, 12, 1), "joao.s@airline.com", "Comissário")
        ]
        crew_team_B = [
            Crewman("Roberto Lima", "444.444.444-44", date(1988, 7, 30), "roberto.l@airline.com", "Piloto"),
            Crewman("Mariana Alves", "555.555.555-55", date(1991, 9, 5), "mariana.a@airline.com", "Copiloto"),
            Crewman("Fernanda Costa", "666.666.666-66", date(1987, 11, 10), "fernanda.c@airline.com", "Comissário")
        ]
        crew_teams = [crew_team_A, crew_team_B]

        data_flights = [
            {"code": "LA-3100", "origin": "São Paulo (GRU)", "destination": "Salvador (SSA)", "horario": datetime(2025, 11, 10, 9, 0)},
            {"code": "LA-3102", "origin": "Rio de Janeiro (GIG)", "destination": "Fortaleza (FOR)", "horario": datetime(2025, 11, 10, 10, 30)},
            {"code": "G3-1400", "origin": "Belo Horizonte (CNF)", "destination": "Recife (REC)", "horario": datetime(2025, 11, 11, 7, 15)},
            {"code": "G3-1404", "origin": "Brasília (BSB)", "destination": "Manaus (MAO)", "horario": datetime(2025, 11, 11, 14, 0)},
            {"code": "AD-2010", "origin": "Campinas (VCP)", "destination": "Porto Alegre (POA)", "horario": datetime(2025, 11, 12, 20, 0)},
            {"code": "AD-2012", "origin": "Curitiba (CWB)", "destination": "Natal (NAT)", "horario": datetime(2025, 11, 12, 21, 45)},
            {"code": "TP-0082", "origin": "Lisboa (LIS)", "destination": "São Paulo (GRU)", "horario": datetime(2025, 11, 13, 11, 0)},
            {"code": "TP-0084", "origin": "Porto (OPO)", "destination": "Rio de Janeiro (GIG)", "horario": datetime(2025, 11, 13, 12, 30)},
            {"code": "IB-6025", "origin": "Madrid (MAD)", "destination": "Salvador (SSA)", "horario": datetime(2025, 11, 14, 16, 0)},
            {"code": "IB-6027", "origin": "Barcelona (BCN)", "destination": "Fortaleza (FOR)", "horario": datetime(2025, 11, 14, 18, 20)}
        ]

        for i, flight_data in enumerate(data_flights):
            airplane_select = self._fleet[i % len(self._fleet)]
            
            flight = Flight(
                code=flight_data["code"],
                origin=flight_data["origin"],
                destination=flight_data["destination"],
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

        print(f"Loading... ")
        time.sleep(2)