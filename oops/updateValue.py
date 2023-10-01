class Update:
    address=""
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    def get_result(self):
        print(f"addres is : {self.address} {self.name} and age is {self.age}")
    def updateValue(self,inputAge):
        self.inputAge=inputAge
        print(f"addres is : {self.address} {self.name} and age is {self.age}")

name1=input("enter your name here : ")     
age1=(input("enter your age here :"))  
address=input("enter your address :")
up=Update(name1,age1,address)
update_age=int(input("enter updated age "))
up.get_result()
up.updateValue(update_age)
