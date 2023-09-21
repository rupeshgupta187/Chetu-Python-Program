import inspect
def exeception_handle(default_response):
    def decorator(func):
        def wrapper(*a,**b):
            try:
                return func(*a,**b)
            except Exception as e:
                 print(f"Exeception has occured {e}")
                 return default_response
        return wrapper
    return decorator
@exeception_handle(default_response="Exception has occures lightly before excution of program") 
def add(a,b):
     div=a/b
     return div
print("the final output is :",add(20,10))


    
