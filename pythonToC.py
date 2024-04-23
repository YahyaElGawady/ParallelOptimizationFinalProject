# Import any necessary modules here

# Define your functions here
def set_up(args, file_name):
    file = open(file_name + ".c", "a")
    file.write("//%%cuda_group_save -n run.cu -g default\n")
    file.write("#include <stdio.h>\n")
    file.write('#include "util.h"\n\n')
    file.write("__host__\n main() {\n")


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
    for name, value in globals().items():
        if value is var:
            return name


def numpy_add_to_c(a, b, result):
    a_name = get_var_name(a)
    b_name = get_var_name(b)
    result_name = get_var_name(result)
    return f"addArraysHelper({a_name}, {b_name}, {result_name})"


def numpy_sub_to_c(a, b, result):
    a_name = get_var_name(a)
    b_name = get_var_name(b)
    result_name = get_var_name(result)
    return f"subtractArraysHelper({a_name}, {b_name}, {result_name})"


def numpy_sum_to_c(a, result):
    a_name = get_var_name(a)
    result_name = get_var_name(result)
    return f"sumArraysHelper({a_name}, {result_name})"


def numpy_dot_product_to_c(a, b, result):
    a_name = get_var_name(a)
    b_name = get_var_name(b)
    result_name = get_var_name(result)
    return f"dotArraysHelper({a_name}, {b_name}, {result_name})"

def set_up_host(args, filen_name, matrix_dim):
    file = open(file_name + ".c", "a")
    file.write("    float *h_input, *h_output;\n")
    file.write(f"    h_input = (float*)malloc({matrix_dim} * {matrix_dim} * sizeof(float));\n")
    file.write(f"    h_output = (float*)malloc({matrix_dim} * {matrix_dim} * sizeof(float));\n")
    
    file.write("    float *d_input, *d_output;\n")
    file.write(f"    cudaMalloc(&d_input, {matrix_dim} * {matrix_dim} * sizeof(float));\n")
    file.write(f"    cudaMalloc(&d_output, {matrix_dim} * {matrix_dim} * sizeof(float));\n\n")

    file.write(f"    cudaMemcpy(d_input, h_input, {matrix_dim} * {matrix_dim} * sizeof(float), cudaMemcpyHostToDevice);\n\n")
    file.write("    THREADS_PER_BLOCK = 256 ;\n")
    file.write("    BlOCKS_PER_GRID = 256 ;\n")
    file.write("    CArraysHelper<<<BLOCKS_PER_GRID, THREADS_PER_BLOCK>>>(args);\n")
    file.write("    cudaDeviceSynchronize();\n\n")

    file.write(f"    cudaMemcpy(h_output, d_output, {matrix_dim} * {matrix_dim} * sizeof(float), cudaMemcpyDeviceToHost);\n\n")

    file.write("    cudaFree(d_input);\n")
    file.write("    cudaFree(d_output);\n")
    file.write("    free(h_input);\n")
    file.write("    free(h_output);\n\n")
    

def main():
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
