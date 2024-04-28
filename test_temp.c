   float h_b[3] = [1, 2, 3];
    float *d_b;
   cudaMalloc(&d_b,3*sizeof(float);
    cudaMemcpy(d_b, h_b,sizeof(h_b), cudaMemcpyHostToDevice);

   float h_a[3] = [1, 2, 3];
    float *d_a;
   cudaMalloc(&d_a,3*sizeof(float);
    cudaMemcpy(d_a, h_a,sizeof(h_a), cudaMemcpyHostToDevice);

