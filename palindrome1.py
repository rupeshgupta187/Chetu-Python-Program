def palindrome(string):
    return string==string[::-1]
string="1234321"
ans=palindrome(string)
if ans:
    print("yes")
else:
    print("No")

z="1234321"
w=" "
for x in z:
    w=x+w
if z==w:
    print(" sorry!! yes")
else:
    print("No")