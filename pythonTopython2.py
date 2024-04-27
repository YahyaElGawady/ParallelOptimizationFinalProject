def setup(file_name):
    file = open(file_name + ".py", "a")
    file.write("import cupy")

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

def array_to_py(variable_name, list_values):
    return f"{variable_name} = cupy.array({list_values.tolist()})"