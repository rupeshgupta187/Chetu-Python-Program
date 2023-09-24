def check_list(expected_type):
    def decorator(func):
        def inner(*a,**b):
            result=func(*a,**b)
            int_type=[]
            # list2=[x for x in result if isinstance(x,expected_type)]
            # return list2

            for x in result:
                if type(x)==int:
                    int_type.append(x)
            return int_type
        return inner
    return decorator

@check_list(int)
def check_integer_type(list):
    list=[1,2,3,4,"rup","hi",3.98,True]
    return list

result=check_integer_type(list)
print(result)
