from datetime import date
from .interface import Person

class Crewman(Person):
    '''
    classe que representa os triuplantes de um voo, herdando da classe Person
    '''
    def __init__(self, name: str, cpf: str, date_of_birth: date, email: str, job: str):
        super().__init__(name, cpf, date_of_birth, email) 
        self._job = job

    @property
    def job(self):
        '''
        retorna um cargo para o tripulante
        '''
        return self._job
    
    def introduce(self):
        '''
        retorna a apresentação escrita do tripulante 
        '''
        return f"{self.job}: {self.name}"