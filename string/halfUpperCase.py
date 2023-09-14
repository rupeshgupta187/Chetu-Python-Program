string=input("enter a string ")

length=len(string)//2
res=""
for x in range(len(string)):
    if x<=length:
        res+=string[x].upper()
    else:
        res+=string[x]

print("the upper half case is :",res)