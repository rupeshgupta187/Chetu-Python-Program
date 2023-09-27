def remove_tuple(tuple):
    tuple=filter(None,tuple)
    return tuple
tuple=[(1,2,3,"rup"),(),()]
x=remove_tuple(tuple)
print(list(x))

def remove_tuple(tuple):
    for i in tuple:
        if len(i)==0:
            tuple.remove(i)
    return tuple
tuple=[(1,2,3,"rup"),(),()]
x=remove_tuple(tuple)
print(list(x))


def remove_tuple(tuple):
    for x in tuple:
        if (x==()):
            tuple.remove(x)
    return tuple
tuple=[(),(1,2,3,"rup"),(),(),()]
x=remove_tuple(tuple)
print(list(x))



