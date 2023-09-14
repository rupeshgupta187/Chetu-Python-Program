c=['C',0,0,0,0,0]

num=input("enter a number")
for x in str(num):
    c.pop()

# c.extend([num])
for x in str(num):
    c.append(x)
for y in c:
    print(y, end="")