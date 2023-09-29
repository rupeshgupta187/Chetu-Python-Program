class car:
    wheels=4
    def __init__(self):
        self.milage=10
        self.name="BMW"
c1=car()
c2=car()

c1.milage=24
print(c1.milage,"Milage and",end=" ")
print(c2.name,"Company is ",end="")