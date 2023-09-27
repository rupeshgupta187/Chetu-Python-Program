def get_num():
    try:
        value1=float(input("enter first number :"))
        value2=float(input("enter second number :"))
        return value1+value2
    except TypeError:
        raise TypeError("Error: invalid data type ")
res=get_num()
print(res)
res1=get_num()
print(res1)