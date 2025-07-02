from interface import Person 

class Crewman(Person):
    
    def __init__(self, name: str, cpf: str, position: str):
        super().__init__(name, cpf)
        self.position = position 
            
    def show(self):
        return f"Crewman: {self.name}"