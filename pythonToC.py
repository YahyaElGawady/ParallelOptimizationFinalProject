# Import any necessary modules here
import inspect
import time
import numpy as np

import parsing_yacc


class Variables:
    variables = ""  #static variable
    var_with_type = ""
    def __init__(self, var, var_type = "float*"):
        if Variables.variables == "":
            Variables.variables += f"d_{var}"
            Variables.var_with_type += f"{var_type} {var}"
        else:
            Variables.variables += f", d_{var}"
            Variables.var_with_type += f", {var_type} {var}"

    @staticmethod
    def get_variables():
        return Variables.variables
    @staticmethod
    def get_var_with_type():
        return Variables.var_with_type

# Define your functions here
def set_up(file_name):
    file = open(file_name + ".c", "a")
    file.write("//%%cuda_group_save -n run.cu -g default\n")
    file.write("#include <stdio.h>\n")
    file.write('#include "util.h"\n')
    file.write('#include "help_file.c"\n\n')
    file.write("__global__\n")
    file.write(f"void {file_name}_kernel(float * d_input, float * d_output, const int matrix_dim)" + "{\n")


def end_kernel(file_name):
    file = open(file_name + ".c", "a")
    file.write("}\n")


def end_main(file_name):
    file = open(file_name + ".c", "a")
    file.write("    return 0;\n}")


def set_up_main(file_name):
    file = open(file_name + ".c", "a")
    file.write("__host__\n int main() {\n")


def set_arr(var_name, var, var_length, file_name):
    file = open(file_name + "_temp.c", "a")
    #actually getting an array
    #arr_string = (np.array_str(var))[6:]
    #if variables == "":
    # variables += f"d_{var}"
    #else:
    #variables += (f", d_{var}")
    #variables = []
    #variables.append(f"d_{var_name}")
    Variables(var_name)
    #file.write(f"   float h_{var_name}[{var_length}] = {var};\n")
    #file.write(f"    float *d_{var_name};\n")
    #file.write(f"   cudaMalloc(&d_{var_name},{var_length}*sizeof(float);\n")
    #transfer_data(var, file_name, True)
    output = f"   float h_{var_name}[{var_length}] = {var};\n"
    output += f"    float *d_{var_name};\n"
    output += f"   cudaMalloc(&d_{var_name},{var_length}*sizeof(float);\n"
    output += transfer_data(var_name, file_name, True)
    #return output
    file.write(output)
    return ""


def deploy_kernel(file_name):
    file = open(file_name + ".c", "a")
    file.write(f"    THREADS_PER_BLOCK = matrix_dim;\n")
    file.write("    BLOCKS_PER_GRID = matrix_dim;\n")
    file.write(f"    {file_name}_kernel<<<BLOCKS_PER_GRID, THREADS_PER_BLOCK>>>({Variables.get_variables()});\n")
    file.write("    cudaDeviceSynchronize();\n\n")


def transfer_data(var_name, file_name, hToD):
    file = open(file_name + ".c", "a")
    if hToD:
        #file.write(f"    cudaMemcpy(d_{var_name}, h_{var_name},sizeof(h_{var_name}), cudaMemcpyHostToDevice);\n\n")
        return f"    cudaMemcpy(d_{var_name}, h_{var_name},sizeof(h_{var_name}), cudaMemcpyHostToDevice);\n\n"
    else:
        #file.write(f"   cudaMemcpy(h_{var_name}, d_{var_name}, sizeof(h_{var_name}), cudaMemcpyDeviceToHost);")
        return f"   cudaMemcpy(h_{var_name}, d_{var_name}, sizeof(h_{var_name}), cudaMemcpyDeviceToHost);\n"


def free_data(var, file_name):
    file = open(file_name + ".c", "a")
    file.write(f"    cudaFree(d_{get_var_name(var)});\n")
    file.write(f"    free(h_{get_var_name(var)});\n")


#    file.write("}\n\n__host__\n")
#    file.write("const int THREADS_PER_BLOCK = 256, BLOCKS = 3;\n\n")
# convert args to c
# convert args from device to host
#    file.write(file_name + "<<<BLOCKS,THREADS_PER_BLOCK>>>(args);\n")
#    file.write("cudaDeviceSynchronize();\n")
# copy from host to device
# free all the variables
#    file.write("return 0;\n}")
def get_var_name(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return ([var_name for var_name, var_val in callers_local_vars if var_val is var])[0]


def numpy_add_to_c(a_name, b_name, result_name):
    #a_name = get_var_name(a)
    #b_name = get_var_name(b)
    #result_name = get_var_name(result)
    return f"addArraysHelper({a_name}, {b_name}, {result_name});\n"


def numpy_sub_to_c(a_name, b_name, result_name):
    #a_name = get_var_name(a)
    #b_name = get_var_name(b)
    #result_name = get_var_name(result)
    return f"subtractArraysHelper({a_name}, {b_name}, {result_name});"


def numpy_sum_to_c(a_name, result_name):
    #a_name = get_var_name(a)
    #result_name = get_var_name(result)
    return f"sumArraysHelper({a_name}, {result_name});"


def numpy_dot_product_to_c(a_name, b_name, result_name):
    #a_name = get_var_name(a)
    #b_name = get_var_name(b)
    #result_name = get_var_name(result)
    return f"dotArraysHelper({a_name}, {b_name}, {result_name});"


def set_up_host(args, file_name, matrix_dim):
    file = open(file_name + ".c", "a")
    file.write("    float *h_input, *h_output;\n")
    file.write(f"    h_input = (float*)malloc({matrix_dim} * {matrix_dim} * sizeof(float));\n")
    file.write(f"    h_output = (float*)malloc({matrix_dim} * {matrix_dim} * sizeof(float));\n")

    file.write("    float *d_input, *d_output;\n")
    file.write(f"    cudaMalloc(&d_input, {matrix_dim} * {matrix_dim} * sizeof(float));\n")
    file.write(f"    cudaMalloc(&d_output, {matrix_dim} * {matrix_dim} * sizeof(float));\n\n")

    file.write(
        f"    cudaMemcpy(d_input, h_input, {matrix_dim} * {matrix_dim} * sizeof(float), cudaMemcpyHostToDevice);\n\n")
    file.write(f"    THREADS_PER_BLOCK = matrix_dim;\n")
    file.write("    BLOCKS_PER_GRID = matrix_dim;\n")
    file.write("    ArraysHelper<<<BLOCKS_PER_GRID, THREADS_PER_BLOCK>>>(d_input, d_output, matrix_dim);\n")
    file.write("    cudaDeviceSynchronize();\n\n")

    file.write(
        f"    cudaMemcpy(h_output, d_output, {matrix_dim} * {matrix_dim} * sizeof(float), cudaMemcpyDeviceToHost);\n\n")

    file.write("    cudaFree(d_input);\n")
    file.write("    cudaFree(d_output);\n")
    file.write("    free(h_input);\n")
    file.write("    free(h_output);\n\n")
    file.close();
def replace_the_kernel_config(file_name):
    with open(f"{file_name}.c", 'r') as file:
        data = file.read()

        data = data.replace(f"void {file_name}_kernel(float * d_input, float * d_output, const int matrix_dim)" + "{\n", f"void {file_name}_kernel({Variables.get_var_with_type()})" + "{\n")
    with open(f"{file_name}.c", 'w') as file:
        file.write(data)

def transfer_data_back_and_free(file_name):
    file = open(file_name + ".c")
    for var in Variables.variables.split(", "):
        file.write(transfer_data(var,file_name, False)+"\n")
    for var in Variables.variables.split(", "):
        free_data(var,file_name)
def main():
    file = open("test.c", "a")
    input = """
    A = np.array([1, 2, 3])
    B = np.array([4, 5, 6])
    C = np.add(A, B)
    """
    #mode = "C"
    #print("mode is C")
    #for line in input.split("\n"):
    #    if line == "":
    #        continue
    #    result = parsing_yacc.main(line, mode)
    #    file.write(result)
    #    print(result)
    set_up('test')

    set_arr("b", "[1, 2, 3]",3, "test")
    set_arr("a", "[1, 2, 3]",3, "test")
    file.write(numpy_add_to_c('a','b','c'))
    end_kernel('test')
    set_up_main('test')
    file_read = open("test_temp.c", 'r')
    for line in file_read:
         file.write(line)
    deploy_kernel('test')
    transfer_data_back_and_free('test')
    end_main('test')
    file.close()
    file_read.close()
    replace_the_kernel_config("test")
    pass

if __name__ == "__main__":
    main()

#helper functions
# __device__ void addArraysHelper(float *array1, float *array2, float *result) {
#     int N = blockDim.x * gridDim.x;
#     for (int i = threadIdx.x + blockIdx.x * blockDim.x; i < N; i += blockDim.x * gridDim.x) {
#         result[i] = array1[i] + array2[i];
#     }
# }
# __global__ void subtractArraysHelper(float *array1, float *array2, float *result) {
#     int N = blockDim.x * gridDim.x;
#     for (int i = threadIdx.x + blockIdx.x * blockDim.x; i < N; i += blockDim.x * gridDim.x) {
#         result[i] = array1[i] - array2[i];
#     }
# }
# __global__ void sumArraysHelper(float *array, float *result) {
#     int N = blockDim.x * gridDim.x;
#     for (int i = threadIdx.x + blockIdx.x * blockDim.x; i < N; i += blockDim.x * gridDim.x) {
#         atomicAdd(result, array[i]);
#     }
# }
