class ATM:
    def __init__(self):
        self.pin=""
        self.balance=0
        self.menu()
    def menu(self):

        option=int(input('''
        How would like to proceesd for further steps
            1. Enter 1 to set pin successfully
            2. Enter 2 for deposite amount
            3. Enter 3 for widthdraw amount
            4. Enter 4 for check balance 
            5. Enter 5 for  exit
        '''))
        if option==1:
            self.Set_pin()
        elif option==2:
            self.deposite()
        elif option==3:
            self.widthdraw()
        elif option==4:
            self.check_balance()
        else:
            exit()

    def Set_pin(self):
            self.pin=input("Enter pin number to set ")
            print("pin set suceesfully")
        
    def deposite(self):
            upi=input("Enter pin :")
            if upi==self.pin:
                amount=int(input("Enter amount for deposite :"))
                self.balance+=amount
                print("amount diposited successfully ")
    def widthdraw(self):
            upi=input("enter pin :")
            if upi==self.pin:
                amount=int(input("Enter amount for widthdraw"))
                self.balance-=amount
                print("Amount dicuted from the account ")
    def check_balance(self):
            upi=input("enter pin")
            if upi==self.pin:
                print("your current balance is :",self.balance)
            

sbi=ATM()


