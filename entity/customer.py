from .interface import Person 
from datetime import date

class Customer(Person):
    '''
    classe usada para representar um cliente/passageiro de um voo, herdando da classe Person
    '''
    def __init__(self, name: str, cpf: str, date_of_birth: date, email: str):
        super().__init__(name, cpf, date_of_birth, email)

    def introduce(self):
        '''
        retorna uma apresentação especifica para o nome do passageiro.
        '''
        return f"Cliente: {self._name}"