from customer import Customer
import string
import random
class Reservation:
    def __init__(self, customer: Customer, seat: int):
        self.customer = Customer
        self.seat = seat
        self.locator = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        pass
    
    def make_checkin(self):
        pass
    
    def cancel(self):
        pass