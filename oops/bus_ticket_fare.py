class Vehicle:
    def __init__(self,name, capicity):
        self.name=name
        self.capicity=capicity
    def fare(self):
        return self.capicity*100
    
class Bus(Vehicle):
    def fare(self):
        amount=super().fare()
        amount+=(amount*10)/100
        return amount
school_bus=Bus("Mahindra",55)
print(school_bus.fare())