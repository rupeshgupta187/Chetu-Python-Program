class student:
    school=""
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    def average(self):
        return (self.m1+self.m2+self.m3)/3
s1=student(12,34,54)
s2=student(956,865,344)

print(s1.average())
print(s2.average())