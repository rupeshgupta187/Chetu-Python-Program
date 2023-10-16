
def check_type(expected_type):
    def decorator(func):
        def inner(*a,**b):
            result=func(*a,**b)
            if not all(isinstance(item,expected_type) for item in result):
                raise TypeError("There is type error ")
            return result
        return inner
    return decorator
@check_type(int)
def int_list():
    n=[1,2,3,4,5]
    return n


x=int_list()
print(x)