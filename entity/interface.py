from abc import ABC 

class Person(ABC):
    def __init__(self, name: str, cpf: str):
        self.name = name
        self.cpf = cpf
    def show(self):
        pass