def convert_to_data_type(data_type):
    def decorator(func):
        def wrapper(*a,**b):
            result=func(*a,**b)
            return data_type(result)
        return wrapper
    return decorator
@convert_to_data_type(int)
def add(x,y):
    return x+y

print(add(20,30) , type(add))
result=add(20,30)
print(result, type(result))

@convert_to_data_type(str)
def conctenate_string(s1,s2):
    return s1+s2

sum_of_string=conctenate_string("Python ","Decorator")
print(sum_of_string,type(sum_of_string))