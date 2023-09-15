def ArmstrongNumber(num):
    temp=num
    rev=0
    while num!=0:
        digit=num%10
        rev=rev+digit**3
        num=num//10
    if rev==temp:
        print(temp," is Armstrong Number ")
    else:
        print(temp," is not a Armstrong number ")


ArmstrongNumber(131)
ArmstrongNumber(153)
