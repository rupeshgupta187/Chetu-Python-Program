num=int(input('enter a number : '))
temp=num
rem=0
while temp>0:
    digit=temp%10
    rem= rem*10+digit
    temp=temp//10
if num==rem:
    print('it is a palindrome')
else:
    print("it is not a palindrome")