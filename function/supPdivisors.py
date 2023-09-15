def sumPdivisors(num):
    divisors=[]
    for x in range(1,num):
        if num%x==0:
            divisors.append(x)
    return sum(divisors)
num=36
print(sumPdivisors(num))