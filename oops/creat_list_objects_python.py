class geeks:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

list=[]
list.append(geeks("Rupesh",1))
list.append(geeks("Aman",2))
list.append(geeks("Shivam",3))
list.append(geeks("Deepak",4))
list.append(geeks("Akash",5))

for obj in list:
    print(obj.name,obj.rollno)
print()
print()
print()
print(list[0].rollno,list[0].name)
print(list[1].rollno,list[1].name)
print(list[2].rollno,list[2].name)
print(list[3].rollno,list[3].name)
print(list[4].rollno,list[4].name)