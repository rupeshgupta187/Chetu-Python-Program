def check_list_type(expected_type):
    def decorator(func):
        def inner(*args,**kwargs):
            result=func(*args,**kwargs)
            if not all(isinstance(item,expected_type) for item in result):
                raise TypeError(f'List items are not same {expected_type.__name__}')
            else:
                print("there are the same data types in the list")
            return result
        return inner
    return decorator

@check_list_type(int)
def check_intger_type(n):
    
    return [i for i in range(n)]
result=check_intger_type(5)
print(result)
print('*'*30)
try:
    string_list=check_intger_type('5')
except Exception as e:
    print("erroe is :",e)


