from abc import ABC, abstractmethod
from datetime import date

class Person(ABC):
    def __init__(self, name: str, cpf: str, date_of_birth: date, email: str):
        self._name = name
        self._cpf = cpf
        self._date_of_birth = date_of_birth
        self.email = email

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
        if isinstance(new_email, str) and "@" in new_email and "." in new_email:
            self._email = new_email
        else:
            raise ValueError(f"ERRO: Email inválido: '{new_email}'.")
    
