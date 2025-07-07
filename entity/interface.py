from abc import ABC, abstractmethod
from datetime import date

class Person(ABC):
    def __init__(self, name: str, cpf: str, date_of_birth: date, email: str):
        self._name = name
        self._cpf = cpf
        self._date_of_birth = date_of_birth
        self._email = email

    @property
    def name(self):
        return self._name

    @property
    def cpf(self):
        return self._cpf

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email: str):
        if "@" in new_email:
            self._email = new_email
        else:
            print("Erro: Formato de email inválido.")
    
    @abstractmethod
    def introduce(self):
        pass

class Authenticable(ABC):
    def __init__(self, password: str):
        self._password = password

    @abstractmethod
    def authenticate(self, password_attempt: str) -> bool:
        pass