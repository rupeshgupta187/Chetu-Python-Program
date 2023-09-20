list=[1,2,3,4,5,6,7,8,9,0]
print("Original list : ",list)
for x in range(len(list)):
    for y in list:
        if x==2:
            list.remove(list[2])
            print(list)

#######################################
list=[1,2,3,4,5,6,7,8,9,0]
while list:
    if len(list)>=3:
        del list[2]
        print(list)



