class Human:
    def __init__(self,name,age):
        print("this is human class constructer ")
        self.name=name
        self.age=age
    def display(self):
        
        print(f"the name is {self.name} and age is {self.age}")
        
    def eat(self):
        print("Human can eat ")
class Female(Human):
    def __init__(self,name,age,can_dance):
        super().__init__(name,age)
        self.know_dance=can_dance
        print("this Female class constructer")

    def display(self):
        print(f"{self.name},{self.age} and she can dance supereb ")
class Male(Human):

    def __init__(self,name,age,location): 
        Human.__init__(self,name,age)
        self.location=location
        print("this is Male class constructer ")

    def display(self):
        return f"{self.name},{self.age},{self.location}"
    
female=Female("Shivani",20,"Noida")
print()
male=Male("Shivam",20,"Noida")
print()
print()
male.display()
female.display()
