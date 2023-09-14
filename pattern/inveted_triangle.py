n=7

for i in range(n+1):
    # inner loop for spaces 
    for j in range(n-i):
        print(" ", end=" ")
    
    # inner loop for star
    for j in range(i):
        print("*", end=" ")

    print()
