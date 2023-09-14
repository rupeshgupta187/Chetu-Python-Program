from collections import Counter
list=[1,2,3,4,5,5,5,6,7,8,]
count=0
a=5
for i in list:
    if i==a:
        count+=1

print("count of 5 is :",count)       
######################################################

l=[1,2,3,4,55,55,5,55,68,8,]
def occurence(list,x):
    return list.count(x)
x=55
print(occurence(l,x))

