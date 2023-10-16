class Parent:
    def overloaded(self,a=None,b=None):
        if a!=0 and b!=0:
            return a+b
        if a!=0:
            return a
        else:
            return "No argument passed"
class child(Parent):
    def overloaded(self,a=None,b=None,c=None):
        if c is not None:
            return a+b+c
        else:
            return super().overloaded(a,b)
        
obj=child()
print(obj.overloaded(1,3))