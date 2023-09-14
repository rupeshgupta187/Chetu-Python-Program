n=7
for i in range(n+1):
    for j in range(1,i):
        print(j, end=" ")
    print()

for k in range(n+1):
    for j in range(2*n-k):
        print(" ", end=" ")

    for i in range(1,k):
        print(i, end=" ")
    
    
    print()
#####################################

# for i in range(n+1):
#     for j in range(1,n-i+1):
#         print(j,end=" ")
#     print()


    