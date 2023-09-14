L=[12,34,56,78,97,14]
l=[]
print("Original list and their element :",L)
for x in L:
    l.insert(0,x)
print(l)
L.reverse()
print(L)

###############################################

def reverse(list):
    new_list=list[::-1]
    return new_list
list=[10,20,30,40,50,60,70]

print(reverse(list))
######################################################

print()
lst=list=[10,20,30,40,50,60,70]
print(lst)
li=lst.copy()
print(li)