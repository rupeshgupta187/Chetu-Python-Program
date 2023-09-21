def check_list_type(expected_type):
    def decorator(func):
        def inner(*a,**b):
            result=func(*a,**b)
            list2=[x for x in result if isinstance(x,int)]
            return list2
        return inner
    return decorator
@check_list_type(int)
def check_integer_type(list):
    list=[1,2,3,4,56,"Hii","Hello"]
    return list
result=check_integer_type(list)
print(result)
            