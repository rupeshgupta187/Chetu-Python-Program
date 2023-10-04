class coffiee:
    
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def budget_check(self,budget):
        
            if not isinstance(budget,(int,float)):
                print("please enter budget in integer")
            if budget<0:
                print("sorry you don't have maney ")
                exit()
       
    def get_change(self,budget):
        if self.price>0:

            return f"change which you get : {abs(self.price - budget)}"
        else:
            print("enter valid price for product ")
    def sell(self,budget):
        if self.price>0:
            if budget>=self.price:
                self.get_change(budget)
                print(f"you can afford the {self.name} coffiee")

                if budget==self.price:
                    print(f"it's complete ")
                else:
                    print(f"here some change of yours {self.get_change(budget)}")
        else:
            print("enter valid price for product")

small=coffiee("big",50)
print(small.get_change(4))
small.sell(364)
print('\n\n')
small.sell(64)
print('\n\n')
small.sell(164)

