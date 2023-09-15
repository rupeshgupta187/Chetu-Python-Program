def swapCheck(a,b):
    print("before swap :",a,b)
    a=a+b
    b=a-b
    a=a-b
    return a,b
a,b=swapCheck(2,9)
print("after the swap :",a,b)
print("after the swap :",swapCheck(2,3))