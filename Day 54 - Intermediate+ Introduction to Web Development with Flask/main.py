import time


def speed_calc_decoration(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed {end_time - start_time}s")
    return wrapper_function


@speed_calc_decoration
def slow_function():
    for _ in range(10):
        pass


@speed_calc_decoration
def fast_function():
    for _ in range(100000000):
        pass


slow_function()
fast_function()
