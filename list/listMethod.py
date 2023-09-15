# nm="Rupesh Gupta"
# print(len(nm))
# print(nm.upper())
# print(nm.lower())
# print(nm.replace("Rupesh","aditya  "))

# for i in range(5):
#     # for j in range(5-i):
#     #     print(" ",end="")
#     for j in range(1,i):
#          print(j,end=" ")

#     for j in range(i-1,0,-1): 
#         print(j,end=" ")
#     print()


# 

n=6
for i in range(n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i - 1, 0, -1):
            print(j, end=" ")
    print()


###################################################

# reverse right angle triaagle 3

for i in range(n+1):
     for j in range(n+1-i or n-i):
          print("*",end="")
     print()