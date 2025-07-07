from .interface import Person, Authenticable
from datetime import date

class Crewman(Person, Authenticable):

    def __init__(self, name: str, cpf: str, date_of_birth: date, email: str, job: str, password: str):
        super().__init__(name, cpf, date_of_birth, email)
        Authenticable.__init__(self, password)

    @property
    def job(self):
        return self._job
    
    def show(self):
        return f"Tripulante: {self.name}, CARGO: {self.job}"
    
    def authenticate(self, try_password: str) -> bool:
        print(f"Autenticando {self.name} como {self.job}...")
        return try_password == self._password
        