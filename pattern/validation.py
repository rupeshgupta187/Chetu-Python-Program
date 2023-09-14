name=input("enter name :").split()
 
# for i in name:
#     for j in range(len(i)):
#         print(i[j].upper(), end="")
        
for i in name:
   for j in range(len(i)):
    if j%2==0:
       print(i[j].upper(),end="")
    else:
       print(i[j].lower(),end="")
