save=0
for i in range(1, 101):
    save=save+i

print("suma of even number : ",save)

# sum of odd natural number \\

sum=0
for i in range(1, 20, 1):
    sum=sum+i
print("sum of odd number : ",sum)

###########################################

fact=1
for i in range(1,6):
    fact=fact*i
print("factorial of nth nth number : ",fact)

print("#############################################")

def Fibonanci(n):
    x=Fibonanci(n-1)+Fibonanci(n-2)
    if n<0:
        print("invalid")
    elif n==1:
        return 1

    else:
        return x
    
print("fibonanaci series of nth number : ",Fibonanci(9))