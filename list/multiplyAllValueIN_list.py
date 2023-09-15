#multiply the number list using travarsal
def multiply(list):
    result=1
    for x in list:
        result=result*x
    return result
list=[1,2,3,4]

print(multiply(list))

# multiply the number using numpy.prod multiplication

import numpy

list=[1,2,3,4,5,6]
list1=[1,2,3,4,5,6,7]
result=numpy.prod(list)
result=numpy.prod(list1)
print(result)