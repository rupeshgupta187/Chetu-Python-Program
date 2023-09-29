for i in range(4):
    for j in range(7):
        if  j==6 or j==0 or i==0 or i==6:
            print("*",end="")
        else:
            print(' ', end="")
    print()