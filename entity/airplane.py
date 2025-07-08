class Airplane:
    '''
    classe que representa o avião
    '''
    def __init__(self, model: str, fabricator: str, register: str, capacity: int):
        self._model = model
        self._fabricator = fabricator
        self._register = register
        self._capacity = capacity
        self._status_operator = 'Operacional'
        
    @property
    def capacity(self):
        '''
        retorna a capacidade do avião 
        '''
        return self._capacity
    
    @property
    def model(self):
        '''
        retorna o modelo do avião
        '''
        return self._model
    
    @property
    def fabricator(self):
        '''
        retorna a fabricante de um avião
        '''
        return self._fabricator
        
    @property
    def register(self):
        '''
        retorna o registro da aeronave
        '''
        return self._register
        
    @property
    def status_operator(self):
        ''' 
        retorna o status do avião, já definido como 'operacional'
        '''
        return self._status_operator
    
    def __str__(self):
        '''
        retorna uma representação escrita do avião e seus atributos 
        
        '''
        return (f"Avião: {self._model}, Fabricante: {self._fabricator}, " f"Registro: {self._register}, Capacidade: {self._capacity}, "f"Status: {self._status_operator}")