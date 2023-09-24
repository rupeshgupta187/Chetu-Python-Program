n=int(input("enter a number is :"))

if (n>=1):
    sum=0
    number=1
    for x in range(n+1):
        sum=sum+x
    print(sum)
else:
    print("enter value 1 to n")

sum1=0
number=1
while number<n+1:
    sum1=sum1+number
    number+=1
print(sum1)

current=1
for x in range(1,6):
    sum=current+x**3
    print(f"{current} + {x**3} =",end="")
    print(sum)
    current=sum