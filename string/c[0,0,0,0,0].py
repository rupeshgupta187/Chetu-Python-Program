c=['C',0,0,0,0,0,0]
num=input("enter the number :")
for x in num:
    c.pop()
for x in str(num):
    c.append(x)

for x in c:
    print(x,end="")