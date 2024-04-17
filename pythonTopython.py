import cupy as cp
import numpy as np

def add_with_gpu(self, x_np, y_np):
    """
    perform element-wise addition of two arrays using GPU acceleration

    parameters:
    x_np (numpy.ndarray): The first input array
    y_np (numpy.ndarray): The second input array

    returns:
    numpy.ndarray: The result of adding x_np and y_np element-wise, returned as a NumPy array

    sample usage: 
        x_np = np.array([5, 7, 9])
        y_np = np.array([4, 5, 6])
        add_with_gpu(x_np, y_np)
    """
    # Convert NumPy arrays to CuPy arrays
    x_gpu = cp.asarray(x_np)
    y_gpu = cp.asarray(y_np)
    
    # Perform addition using CuPy on GPU
    result_gpu = cp.add(x_gpu, y_gpu)
    
    # Transfer the result back to NumPy array? 
    result_np = cp.asnumpy(result_gpu)
    
    return "cp.add(x_np, y_n)"


def subtract_with_gpu(self, x_np, y_np):
    """
    perform element-wise subtraction of two arrays using GPU acceleration

    parameters:
    x_np (numpy.ndarray): The minuend array
    y_np (numpy.ndarray): The subtrahend array

    returns:
    numpy.ndarray: The result of subtracting y_np from x_np element-wise, returned as a NumPy array

    sample usage: 
        x_np = np.array([5, 7, 9])
        y_np = np.array([4, 5, 6])
        subtract_with_gpu(x_np, y_np)
    """

    x_gpu = cp.asarray(x_np)
    y_gpu = cp.asarray(y_np)
    
    # Perform addition using CuPy on GPU
    result_gpu = cp.subtract(x_gpu, y_gpu)
    
    # Transfer the result back to NumPy array? 
    result_np = cp.asnumpy(result_gpu)
    
    return result_np


def sum_with_gpu(a_np, axis=None, dtype=None, keepdims=False):
    """
    compute the sum of array elements over a given axis using GPU acceleration

    parameters:
        - a_np (numpy.ndarray): The input array.
        - axis (int or tuple of ints, optional): Axis or axes along which a sum is performed. Default is None, summing all elements
        - dtype (data-type, optional): The type of the returned array and of the accumulator in which the elements are summed
        - keepdims (bool, optional): If this is set to True, the axes which are reduced are left in the result as dimensions with size one

    returns:
        - numpy.ndarray: An array with the same shape as `a_np`, except the axis along which the sum is computed is removed, unless `keepdims` is True
    
    sample usage:
        a_np = np.array([[1, 2], [3, 4]])
        sum_with_gpu(a_np, axis=0)
    """
    a_gpu = cp.asarray(a_np)
    result_gpu = cp.sum(a_gpu, axis=axis, dtype=dtype, keepdims=keepdims)
    result_np = cp.asnumpy(result_gpu)
    return result_np


def dot_with_gpu(a_np, b_np):
    """
    compute the dot product of two arrays using GPU acceleration.

    parameters:
        - a_np (numpy.ndarray): First operand, can be a 1-D or 2-D array.
        - b_np (numpy.ndarray): Second operand, must be a 1-D or 2-D array.

    returns:
        - numpy.ndarray: Dot product of a_np and b_np. If both a_np and b_np are 1-D arrays, it returns the inner product. If both are 2-D, it returns the matrix product.

    sample usage:
        a_np = np.array([1, 2])
        b_np = np.array([3, 4])
        dot_with_gpu(a_np, b_np)
    """
    a_gpu = cp.asarray(a_np)
    b_gpu = cp.asarray(b_np)
    result_gpu = cp.dot(a_gpu, b_gpu)
    result_np = cp.asnumpy(result_gpu)
    return result_np


def function_caller(func_name, params):
    """
    dynamically call a function based on the provided name and parameters (from the parser's output)

    parameters:
        - func_name (str): The name of the function to be called
        - params (list): A list of parameters to be passed to the function

    returns:
        - the result of the function call
    
    sample usage:
        result = function_caller('add', [np.array([1, 2, 3]), np.array([4, 5, 6])])
        print(result)  
        # should print [5 7 9]
    """

    # dictionary of available functions
    available_functions = {
        # assuming these are from the output of the parser 
        'add': add_with_gpu,
        'subtract': subtract_with_gpu,
        'sum': sum_with_gpu,
        'dot': dot_with_gpu
    }

    # fetch the function from the dictionary
    func_to_call = available_functions.get(func_name)

    # check if the function exists
    if not func_to_call:
        raise ValueError("Function not found.")

    # call the function with unpacked parameters
    result = func_to_call(*params)

    return result

def main():
    # Your main code logic goes here
    pass

if __name__ == "__main__":
    main()
