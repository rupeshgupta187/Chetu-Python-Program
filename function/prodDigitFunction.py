def prodDigit(num):
    
    prod=1
    while num>0:
        digit=num%10
        prod*=digit
        num//=10
    return prod
num=55
print(prodDigit(num))