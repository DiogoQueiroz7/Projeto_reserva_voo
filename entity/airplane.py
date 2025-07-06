class Airplane:
    def __init__(self, model: str, fabricator: str, register: str, capacity: int):
        self.model = model
        self.fabricator = fabricator
        self.register = register
        self.capacity = capacity
        self.status_operator = 'Operacional'
        
    @property
    def capacity(self):
        return self._capacity
    
    @property
    def model(self):
        return self._model
    
    def __str__(self):
        return f"Avião: {self.model}, Fabricante: {self.fabricator}, Registro: {self.register}, Capacidade: {self.capacity}, Status: {self.status_operator}"
    