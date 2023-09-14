n=10

for i in range(n):
    for j in range(i+1):
        sum=i+j
        if sum%2==0:
            print("1", end=" ")
        else:
            print("0",end=" ")
    print()
