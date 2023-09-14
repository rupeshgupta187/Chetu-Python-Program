n=int(input("enter a number :"))
count=0
i=1
while i<=n:
    if n%i==0:
        count+=1
    i+=1
if count==2:
    print("prime ")
else:
    print("not prime")

################################################################
def primeNumber():
    num=int(input("enter number : "))
    for i in range(2, num):
        if num%i==0:
            print("not number ")
            break    
    else:
            print(" prime ")
    
primeNumber()



###########################################################
