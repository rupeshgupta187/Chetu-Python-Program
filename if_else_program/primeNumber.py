num=int(input("enter a number is :"))
flag=False
for i in range(2,num):
    if(num%i==0):
        flag=True
if flag:
    print("it not a prime a number ")
else:
    print(" it is a prime number")