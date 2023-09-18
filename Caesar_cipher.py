def rotate_char(c):
    rot_by=3
    c=c.lower()
    alphabet="abcdefghijklmnopqrstuvwxyz"
    if c not in alphabet:
        return c
    rotated_pos=ord(c)+rot_by

    if rotated_pos<=ord(alphabet[-1]):
        return chr(rotated_pos)
    return chr(rotated_pos-len(alphabet))
c=input("""Enter a your massage and 
           don't worry no one can see 
           the original message " : """)
res="".join(map(rotate_char,c))
print(res)