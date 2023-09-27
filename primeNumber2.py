# # num=int(input("enter a number : "))
# # flag=False

# # while num>1:
# #     for i in range(2,num):
# #         if num%i==0:
# #             flag=True
# #             break
        

# # if flag:
# #     print("it not a prime number : ")
# # else:
# #     print("it a prime number ")

# start=int(input("ENter starting number :"))
# end=int(input("enter ending number :"))
# count=0
# sum=0
# list=[]

# for i in range(start,end):
#     flag=0
#     for j in range(2, i//2+1):
#         if i%j==0:
#             flag=1
#         else:
#             flag=0
#     if flag==0:
#         list.append(i)
#         count+=1
# for i in range(len(list)):
#     sum=sum+list[i]
# print("sum of prime element number is : ", sum)
# print("list of prime nuber is ",list)
# print("count of prime number is ",count)

list=[]
count=0
flag=0
for i in range(1,100):
   
    for j in range(2,i//2+1):
            if i%j==0:
                flag=1
                break
            else:
                flag=0
    if flag!=1:
        list.append(i)
        count+=1
print(list)
print(count)
# for i in range(len(list)):
     
  
  
   