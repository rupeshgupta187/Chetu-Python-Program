import time
def measure_time(func):
    def wrapper(*a,**b):
        start_time=time.time()
        result=func(*a,**b)
        end_time=time.time()
        calculated_time=end_time-start_time
        return result
    return wrapper

@measure_time
def slowzfunction():
    return time.sleep(2)
slowzfunction()
