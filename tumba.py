import inspect
import ctypes

def generate_so_file(func_name):
    pass

def compile(func):
    func_info = inspect.getsource(func)
    func_info=func_info.split('\n')
    func_info=func_info[1::]
    func_info="\n".join(func_info)
    so_file = generate_so_file(func.__name__,func_info)
    so_text = open(so_file, 'rb').read()
    c_functions = ctypes.CDLL(so_file)
    return c_functions[func.__name__]
