def remove(list):
    for i in list:
        if(i==()):
            list.remove(i)
    return list
list=[(),(),1,3,4,"Rupesh",("ram",1,3,4),()]

print(remove(list))

print("##############################################")

############################################################
b=[]
for x in list:
    if(type(x)==tuple and len(x)==0):
        continue
    if type(x)==tuple and len(x)==0:
        list.remove(i)
    b.append(x)

print(list)
print("**********************************************")
print(b)