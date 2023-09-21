import time 


def measure_exectuion_time(fun):
    def inner(*arg,**kward):
        start_time=time.time()
        result=fun(*arg,**kward)
        end_time=time.time()
        execution_time=end_time-start_time
        print(f'funtion {fun.__name__} took {execution_time:4f} second to execute')
        return result
    return inner
@measure_exectuion_time
def calculate_multiply(number):
    tot=1
    for x in number:
        tot*=x
    return tot

x=calculate_multiply((10,20,30,40,50))
print(x)