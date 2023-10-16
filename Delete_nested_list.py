# s={1,22,3,24,5,6,}
# l=list(s)
# l.sort()
# print(l)

empty=[]
slist=[1,23,4,5,6,[34,56,778,87],[34,433, [34,657,87]]]
# for x in range(len(slist)):
#     if type(slist[x])==list:
       
#         continue
#     empty.append(x)
# print(empty)

# print()
print()

for x in slist:
    if type(x)==list:
       
        continue
    empty.append(x)
print(empty)


def decorator(arg):
    def inner(a):
        result=a.upper()
        return result
    return inner
@decorator
def string(a):
    return a
x=string("rupesh")
print(x)

x=(12,34,45,[45,545,56])
x[3][2]=00
print(x)



