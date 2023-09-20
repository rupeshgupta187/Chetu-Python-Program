def validateFunct(condition):
    def decorator(func):
        def wrapper(*arg,**kwrgs):
            if condition(*arg,**kwrgs):
                return func(*arg,**kwrgs)
            else:
                raise ValueError("Invalidi argument passed in the function parameter!!")
        return wrapper
    return decorator

@validateFunct(lambda x: x > 0 )
def calculatecube(x):
    return x**3


cube=calculatecube(5)
print(type(cube))
print(cube)


