from abc import ABC 
from datetime import date


class Person(ABC):
    def __init__(self, name: str, cpf: str, date_of_birth: date, email: str  ):
        self.name = name
        self.cpf = cpf
        self.date_of_birth = date_of_birth
        self.email = email
        
    @property
    def name(self): return self._name
    @property
    def cpf(self): return self._cpf
    @property
    def date_of_birth(self): return self._date_of_birth
    @property
    def email(self): return self._email

    @email.setter
    def email(self, new_email: str):
        if "@" in new_email: self._email = new_email
        else: print("Erro. Email digitado incorretamente!")
        
class Authenticable(ABC):
    def __init__(self, password: str):
        self.password = password
    def authenticate(self, try_password: str) -> bool:
        return self.password == try_password