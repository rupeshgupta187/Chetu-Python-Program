#write a python programs to wsap first and lat element of the list 
#*****Approach--- find the length of the list and simply swap the first element with (n-1)th element
list=[12,33,45,55,66]
size=len(list)

temp=list[0]
list[0]=list[size-1]
list[size-1]=temp
print(list)

def swapList(newList):     
    newList[0], newList[-1] = newList[-1], newList[0]
    return newList
# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))

###################################

list=[1,22,33,44,55,66]

first=list.pop(0)
last=list.pop(-1)
list.insert(0,last)
list.append(first)
print(list)

###########################################

def swap(list):
    first,*middle, last=list
    list=[last,*middle,first]
    
    return list
list=[21,43,65,76,87,]
print(swap(list))