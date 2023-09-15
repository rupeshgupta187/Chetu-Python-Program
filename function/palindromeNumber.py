def PalindromeNumber(num):
    temp=num
    rev=0
    while num!=0:
        r=num%10
        rev=rev+r
        num=num//10

    if temp==rev:
        print(temp,"it is palindrome number ")
    else:
        print(temp,"is not a palindrome number ")
PalindromeNumber(131)
PalindromeNumber(132)