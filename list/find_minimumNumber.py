list=[]

num=int(input("enter a number to add in the list :"))

for x in range(1,num+1):
    element=int(input("enter a number : "))
    list.append(element)
print('smallest number is :',min(list))