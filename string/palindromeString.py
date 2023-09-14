def isPalindrome(s):

    return s==s[::-1]
s=input("enter text to check palindrome is or not : ")
ans=isPalindrome(s)

if ans:
    print("it is palindrome")
else:
    print("it is not a palindrome")

####################################################


x="12321"

w=""
for i in x:
    w=w+i
if x==w:
    print("it is a palindrome")
else:
    print("it is not a palindrome number")

####################################################

st=input("enter a text : ")
j=-1
flag=0
for i in x:
    if  i != st[j]:
        flag=1
        break
    j=j-1
if flag==1:
    print("Not palindrome ")
else:
    print("palindrome ")