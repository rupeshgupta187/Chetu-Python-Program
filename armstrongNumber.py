num=int(input("Enter a number :"))
reverse=0
temp=num
while temp>0:
    reminder=temp%10
    reverse=reverse*10+reminder
    temp=temp//10
if num==reverse:
    print("Palindrome Number :")
else:
    print("Not prime")

a=10
print(dir(a))