def secret_language(input):
    rot_by=3
    input=input.lower()
    alphabet="abcdefghijklmnopqrstuvwxyz"
    if input not in alphabet:
        return input
    
    rot_pos=ord(input)+rot_by
    if rot_pos<=ord(alphabet[-1]):
        return chr(rot_pos)
    
    return chr(rot_pos+rot_by)
input=input("enter a charater for secret code : ")
res="".join(map(secret_language,input))
print(res)
