class Airplane:
    def __init__(self, model: str, fabricator: str, register: str, capacity: int):
        self._model = model
        self._fabricator = fabricator
        self._register = register
        self._capacity = capacity
        self._status_operator = 'Operacional'
        
    @property
    def capacity(self):
        return self._capacity
    
    @property
    def model(self):
        return self._model
    
    @property
    def fabricator(self):
        return self._fabricator
        
    @property
    def register(self):
        return self._register
        
    @property
    def status_operator(self):
        return self._status_operator
    
    def __str__(self):
        return (f"Avião: {self._model}, Fabricante: {self._fabricator}, " f"Registro: {self._register}, Capacidade: {self._capacity}, "f"Status: {self._status_operator}")