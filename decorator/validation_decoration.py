def validate_decorator(func):
    def wrapper(*a,**b):
        result=func(*a,**b)
        print(type(result))
        for x in a:
            if not isinstance(x,int):
                raise ValueError("Invalid input is passed ")
        return result
            
    return wrapper





@validate_decorator
def multiply(a,b):
    return a*b
output=multiply(2,7)
print(output)

