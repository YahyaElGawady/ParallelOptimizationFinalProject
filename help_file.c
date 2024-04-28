//%%cuda_group_save -n util.h -g default
//helper functions
__device__ void addArraysHelper(float *array1, float *array2, float *result) {
     int N = blockDim.x * gridDim.x;
     for (int i = threadIdx.x + blockIdx.x * blockDim.x; i < N; i += blockDim.x * gridDim.x) {
         result[i] = array1[i] + array2[i];
     }
}
__global__ void subtractArraysHelper(float *array1, float *array2, float *result) {
     int N = blockDim.x * gridDim.x;
     for (int i = threadIdx.x + blockIdx.x * blockDim.x; i < N; i += blockDim.x * gridDim.x) {
         result[i] = array1[i] - array2[i];
     }
 }
 __global__ void sumArraysHelper(float *array, float *result) {
     int N = blockDim.x * gridDim.x;
     for (int i = threadIdx.x + blockIdx.x * blockDim.x; i < N; i += blockDim.x * gridDim.x) {
         atomicAdd(result, array[i]);
     }
 }
 __global__ void dotArraysHelper(float *array1, float *array2, float *result) {
	__shared__ float cache[threadsPerBlock];
	int tid = threadIdx.x + blockIdx.x * blockDim.x;
	int cacheIndex = threadIdx.x;

	float temp = 0;
	while (tid < N){
		temp += a[tid] * b[tid];
		tid += blockDim.x * gridDim.x;
	}

	// set the cache values
	cache[cacheIndex] = temp;

	// synchronize threads in this block
	__syncthreads();

	// for reductions, threadsPerBlock must be a power of 2
	// because of the following code
	int i = blockDim.x/2;
	while (i != 0){
		if (cacheIndex < i)
			cache[cacheIndex] += cache[cacheIndex + i];
		__syncthreads();
		i /= 2;
	}

	if (cacheIndex == 0)
		c[blockIdx.x] = cache[0];
 }
 "output = np.add(array1, array2" --> output, array1, array2
 //float* output;
 //addArraysHelper(array1, array2, output);
