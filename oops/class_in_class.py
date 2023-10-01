class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap=self.computer("Hp","i5",12)
    
    def show(self):
        print(f"{self.name}({self.rollno})")
        self.lap.show()

    class computer:

        def __init__(self,brand,cpu,ram):
            self.brand=brand
            self.cpu=cpu
            self.ram=ram
        def show(self):
            print("laptop config is -> ",end="")
            print(self.brand,self.cpu,self.ram)


s1 = Student("rupesh", 19)
s2 = Student("shivam", 18)
s1.show()