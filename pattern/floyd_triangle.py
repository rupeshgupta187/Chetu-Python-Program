n=5

for i in range(1,n+1):
    for j in range(i):
        j+=i
        print(j, end="   ")
    print()

################ second method to solve this problem

number =1
n=5
for i in range(n+1):
    for j in range(i):
       print(number, end=" ")
       number+=1
    print()
   