class Vehicle:
    def __init__(self,name,max_speed,milage):
        self.name=name
        self.max_speed=max_speed
        self.milage=milage
        
    def seating_capicity(self,capicity):
        print(f"the seating capicitty of bus is {capicity}")
    
class Bus(Vehicle):
    def seating_capicity(self, capicity=50):
        return super().seating_capicity(capicity)
    
school_bus=Bus("Volvo",180,20)
school_bus.seating_capicity()