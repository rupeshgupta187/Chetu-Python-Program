def get_num(prompt):
    try:
        value=int(input(prompt))
        return value
    except TypeError:
        raise TypeError("invalid the type of input")
n1=get_num("enter first number ")
n2=get_num("enter second error")
print(n1+n2)