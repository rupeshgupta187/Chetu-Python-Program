# pytho programs to sort the string in acceinding order

string=input("enter some string : ")
list=[]
list2=[]
for x in string:
    y=ord(x)
    list.append(y)
list.sort()
for x in list:
    y=chr(x)
    list2.append(y)
print(list2)
asc_number=" ".join(list2)
print(asc_number)