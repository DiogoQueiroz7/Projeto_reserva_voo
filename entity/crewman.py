from datetime import date
from .interface import Person

class Crewman(Person):
    def __init__(self, name: str, cpf: str, date_of_birth: date, email: str, job: str):
        super().__init__(name, cpf, date_of_birth, email) 
        self._job = job

    @property
    def job(self):
        return self._job
    
    def introduce(self):
        return f"{self.job}: {self.name}"