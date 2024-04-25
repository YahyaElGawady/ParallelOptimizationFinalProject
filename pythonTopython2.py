import numpy as np

def get_var_name(var):
    for name, value in globals().items():
        if value is var:
            return name

def numpy_add_to_py(a, b):
    a_name = get_var_name(a)
    b_name = get_var_name(b)
    return f"cupy.add({a_name}, {b_name})"

def numpy_subtract_to_py(a, b):
    a_name = get_var_name(a)
    b_name = get_var_name(b)
    return f"cupy.subtract({a_name}, {b_name})"

def numpy_sum_to_py(a):
    a_name = get_var_name(a)
    return f"cupy.sum({a_name})"

def numpy_dot_to_py(a, b):
    a_name = get_var_name(a)
    b_name = get_var_name(b)
    return f"cupy.dot({a_name}, {b_name})"