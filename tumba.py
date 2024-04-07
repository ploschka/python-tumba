import inspect
import ctypes
import pycom_api
import timeit
import numba

def generate_so_file(func_name, func_info):
    with open(func_name+".py", 'w') as f:
        f.write(func_info)    
    compiled_file = pycom_api.compile_and_put_in(func_name+".py",func_name+"_")
    return func_name+"_output.so"

def compile(func):
    func_info = inspect.getsource(func)
    func_info=func_info.split('\n')
    func_info=func_info[1::]
    func_info="\n".join(func_info)
    so_file = generate_so_file(func.__name__,func_info)
    funcs = ctypes.CDLL("./"+so_file)
    func = funcs[func.__name__]
    func.restype=ctypes.c_float
    func.argtypes = [ctypes.c_float]
    return func

@compile
def fib(n : int) -> int:
    a : int = 0
    b :int = 1
    i : int= 0
    while i<n:
        b = a+b
        a = b-a
        i = i + 1
    return b


def fib2(n : int) -> int:
    a : int = 0
    b :int = 1
    i : int= 0
    while i<n:
        b = a+b
        a = b-a
        i = i + 1
    return b

@numba.njit()
def fib3(n : int) -> int:
    a : int = 0
    b :int = 1
    i : int= 0
    while i<n:
        b = a+b
        a = b-a
        i = i + 1
    return b

print(fib(40))

print(timeit.timeit(lambda: fib(40), number=10))
print(timeit.timeit(lambda: fib2(40), number=10))
print(timeit.timeit(lambda: fib3(40), number=10))

print("============================")

print(timeit.timeit(lambda: fib(40), number=10))
print(timeit.timeit(lambda: fib2(40), number=10))
print(timeit.timeit(lambda: fib3(40), number=10))

print("============================")

print(timeit.timeit(lambda: fib(40), number=10))
print(timeit.timeit(lambda: fib2(40), number=10))
print(timeit.timeit(lambda: fib3(40), number=10))
