# Import any necessary modules here

# Define your functions here
def set_up (args, file_name):
    file = open(file_name + ".c", "a")
    file.write("#include <stdio.h>\n")
    file.write("#include <cuda_runtime.h>\n\n")
    file.write("__global__ void " + file_name + "(int [][] args) {\n")
    # parse through the function
    file.write("}\n\n__host__\n")
    file.write("int main() {\n")
    file.write("const int THREADS_PER_BLOCK = 256, BLOCKS = 3;\n\n")
    # convert args to c
    # convert args from device to host
    file.write(file_name + "<<<BLOCKS,THREADS_PER_BLOCK>>>(args);\n")
    file.write("cudaDeviceSynchronize();\n")
    # copy from host to device
    # free all the variables
    file.write("return 0;\n}")
def args_to_c:
    #convert python args to c
    #numpy
def main():





    pass

if __name__ == "__main__":
    main()