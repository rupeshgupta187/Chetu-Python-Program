# first=0
# second=1
# third=first+second
# print(third)
# n=5
# count=0

# for x in range(5):
#     third=first+second
#     first=second
#     second=third
#     print(second)

# while count<n:
#     third=first+second
#     first=second
#     second=first
#     count+=1

# numbers = [1, 2, 3, 4, 5]

# for num in numbers:
#     if num != 3 or num != 4:
#         print("Number is not 3 or 4:", num)
#     else:
#         print("Number is 3 or 4:", num)
#         break

x=1
while True:
        print(x)
        x=x+1
        ch=input("Do you want to continue :")
        if (ch!='y' or  ch!='Y'):
            print("breka invoke")
            break
