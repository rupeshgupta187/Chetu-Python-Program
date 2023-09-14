n=4
m=5
for i in range(n+1):
    for j in range(m+1):
        if (i==0 or j==0 or i==n or j==m):
            print("*", end="")
        else:
            print(" ",end="")
    print()