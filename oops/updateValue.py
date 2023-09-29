class Update:
    address=""
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def get_result(self):
        print(f"addres is : {self.address} {self.name}and age is {self.age}")
    def updateValue(self):
        self.age=39
        print(f" update age is {self.age}")

name1=input("enter your name here : ")     
age1=(input("enter your age here :"))  
up=Update(name1,age1)
up.get_result()
up.updateValue()
