def factorial(num):
    fact=1
    while num!=0:
        fact*=num
        num=num-1
    print("the factorial number is :",fact)
factorial(7)

# .<!-- factorial using for loop in the python-->

factorial=1 
num=7
for i in range(1,num + 1):
       factorial = factorial*i
print("The factorial of",num,"is",factorial)

