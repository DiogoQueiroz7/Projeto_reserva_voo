from interface import Person 
from datetime import date

class Customer(Person):

    def __init__(self, name: str, cpf: str, date_of_birth: date, email: str):
        super().__init__(name, cpf, date_of_birth, email)

    def show(self):
        return f"Cliente: {self.name}"