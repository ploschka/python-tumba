import inspect
import ctypes
import pycom_api
import os
import typing

def get_type(python_type):
    if python_type==int:
        return ctypes.c_float
    elif python_type==str:
        return ctypes.c_char_p
    return ctypes.c_void_p

def generate_so_file(func_name, func_info):
    tempdir = './__pycache__'
    temp_py_path=tempdir+'/'+func_name+".py"
    temp_so_path=tempdir+'/'+func_name+"_"
    with open(temp_py_path, 'w') as f:
        f.write(func_info)    
    flag = pycom_api.compile_and_put_in(temp_py_path,temp_so_path)
    os.remove(temp_py_path)
    os.remove(temp_so_path+'output.o')
    return temp_so_path+"output.so"

def compile(func):
    if not os.path.exists("./__pycache__"):
        os.mkdir("__pycache__")
    func_info = inspect.getsource(func)
    func_info=func_info.split('\n')
    func_info=func_info[1::]
    func_info="\n".join(func_info)
    so_file = generate_so_file(func.__name__,func_info)
    funcs = ctypes.CDLL(so_file)
    ret_func = funcs[func.__name__]
    argtypes=[]
    for arg in func.__annotations__:
        if arg=='return':
            break
        argtypes.append(get_type(func.__annotations__[arg]))
    ret_func.restype=get_type(func.__annotations__['return'])
    ret_func.argtypes = argtypes
    return ret_func

#@compile                                              #ret void
#def fib(zcds1 : str, n : int, abcd: int) -> str:
#    return zcds1
#@compile                                             # 1 argument failure
#def fib(zcds1 : str, n : int, abcd: int) -> int:
#    return n*abcd

@compile                                             
def fib(n : int) -> int:
    a : int = 0
    b : int = 1
    i : int = 0
    while i < n :
        b = a + b
        a = b - a
        i = i + 1
    return a

print(fib(50))