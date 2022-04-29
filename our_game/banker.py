
class Banker:

    def __init__(self, balance=0, shelved=0):
        self.balance = balance
        self.shelved = shelved

    def shelf(self, shelved=0):
        self.shelved = shelved
        

    def bank(self, shelved=0, balance=0):
        self.balance += self.shelved
        self.shelved = 0

    def clear_shelf(self):
        self.shelved = 0
        
