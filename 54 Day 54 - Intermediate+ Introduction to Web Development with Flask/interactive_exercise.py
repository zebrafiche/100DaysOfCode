import time

# current_time = time.time()
# print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        print(function.__name__)
        time_before = time.time()
        function()
        time_after = time.time()
        print(time_after-time_before)
    return wrapper_function


# with syntactic sugar
@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


# w/o synctactic sugar
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_func_time = speed_calc_decorator(slow_function)
slow_func_time()
