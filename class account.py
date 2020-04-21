class Account:
    def __init__(self,owner,amount):
        self.owner = owner
        self.amount = amount
    def __str__(self):
        return f"Account owner : {self.owner}\nAccount balance : ${self.amount}"
    def deposit(self,deposit):
        self.amount = self.amount + deposit
        return f"Deposit of ${deposit} accepted and current balance is ${self.amount}"
    def withdraw(self,withdraw):
        if withdraw > self.amount:
            return f"Funds unavailable! Current balance is ${self.amount}"
        else:
            self.amount = self.amount - withdraw
            return f"withdrawal of ${withdraw} accepted and current balance is ${self.amount}"  