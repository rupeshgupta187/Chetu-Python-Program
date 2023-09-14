a=10
b=20

print("Value of A =",a)
print("Value of B is =",b)

c=a
a=b
b=c
print("Value of A =",a)
print("Value of B is =",b)

print("#####################################################")
n = int(input("Enter the number of rows: "))
for i in range(n, 0, -1):
    print("*" * i)


marks=[22, 55,77,99]
index=0
for marks in marks:
        print(marks)
        if index==3:
            print("Awesome rupesh!",end="")
        index+=1
