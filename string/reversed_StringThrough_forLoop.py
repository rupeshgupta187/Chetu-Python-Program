def reversed(s):
    str=""
    for i in s:
        str=i+str
    return str
s="geeksforgeeks"
print("the reversed string is :",reversed(s),end="")
print()


def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

input_string = "rup"
reversed_string = reverse_string(input_string)
print(reversed_string)