from interface import Person 

class Customer(Person):
        
    def show(self):
        return f"Costumer: {self.name}"