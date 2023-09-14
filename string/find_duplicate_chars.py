def find_duplicate_chars(string):
    unique_chars=set()
    duplicate_chars=set()

    for char in string:
        if char in unique_chars:
            duplicate_chars.add(char)
        else:
            unique_chars.add(char)
    return duplicate_chars

print(find_duplicate_chars("geeksforgeejks"))



def duplicate_chars(input):
    unique_char=[]
    duplicate_char=[]
    for i in input:
        if i in  unique_char:
            duplicate_char.append(i)
       
    return duplicate_chars

print(duplicate_chars("geeksforgeeks"))
