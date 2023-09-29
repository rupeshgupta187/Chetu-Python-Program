class calculator:
    def __init__(self,num1,num2):
        self.number1=num1
        self.number2=num2
    def sum(self):
        return self.number1+self.number2
    def sub(self):
        return self.number1-self.number2
    def div(self):
        if self.number2==0:
            return (f"we can not devided be zero {self.number2}")
        return self.number1/self.number2
    def mul(self):
        return self.number1*self.number2
calc=calculator(23,45)
print(calc.sum())
print(calc.sub())
print(calc.mul())
print(calc.div())
print()
print()
calc2=calculator(87,45)
print(calc2.sum())
print(calc2.sub())
print(calc2.mul())
print(calc2.div())






