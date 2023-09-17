s1=set([1,2,3,4,"ram", "raja","rupesh"])
s1.pop()
print(s1)
s1.clear()
print(s1)
try:
    del s1
    print(s1)
except NameError:
    print("set is deleted by programmer in last operation")


s2=set([1,2,3,"ram", "raja","rupesh"])
print(s2)