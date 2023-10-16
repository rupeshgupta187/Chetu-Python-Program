class Example:
    __a=23

    def display(self):
        return self.__a
class child(Example):
    def display1(self):
        return super().display()
    def display2(Example):
        return obj._Example__a
obj=child()
print(obj.display1())
print(obj.display2())