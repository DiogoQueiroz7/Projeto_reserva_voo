from datetime import date
from .interface import Person, Authenticable

class Crewman(Person, Authenticable):
    def __init__(self, name: str, cpf: str, date_of_birth: date, email: str, job: str, password: str):
        Person.__init__(self, name, cpf, date_of_birth, email)
        Authenticable.__init__(self, password)
        
        self._job = job

    @property
    def job(self):
        return self._job
    
    def introduce(self):
        return f"{self.job}: {self.name}"
    
    def authenticate(self, password_attempt: str) -> bool:
        return password_attempt == self._password