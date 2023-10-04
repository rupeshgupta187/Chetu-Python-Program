class Bank:
    def __init__(self,name=None,balance=0):
        self.name=name
        self.balance=balance

    def get_balance(self):
        return self.balance
    def deposit_balance(self,amount=0):
        self.balance+=amount

    def withdraw(self,amount=0):
        self.balance-=amount

class SavingAcount(Bank):
    def __init__(self,name=None,balance=0,interestRate=0):
        super().__init__(name,balance)
        self.interestRate=interestRate

    def interestAmount(self):
        amount=(self.balance*self.interestRate)/100
        return amount
user=SavingAcount("rupesh",5000,5)
print(user.get_balance())
user.deposit_balance(20000)
print(user.get_balance())
print(user.interestAmount())
