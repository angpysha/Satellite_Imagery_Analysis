# Setup and run

1. Set up **WSL** https://docs.microsoft.com/en-us/windows/wsl/install. Need to select Ubuntu last version
2. Enable NVIDIA CUDA on WSL https://docs.microsoft.com/en-us/windows/ai/directml/gpu-cuda-in-wsl.
https://developer.nvidia.com/cuda-downloads
4. Set up nvidia docker https://github.com/NVIDIA/nvidia-docker
5. Download dataset, create dir **shared** on Ubuntu home user directore
6. Start docker service ``sudo service docker start``
7. Run tensorflow container 
7. 
``sudo docker run -it --rm -p 8888:8888 angpysha/mytfgpu:1.0.6 -v ~/shared:/tmp/shared``
7. Setup Pycharm or other internpreter to notebook server localhost:8888

## How to enter bash to docker
1. Find container id using
``sudo docker container list``
2. Run command ``sudo docker exec -it {containerId} /bin/bash``

## How to commit new changes to docker container
1. Find current running container ID using command ``sudo docker container list``
2. Create new version of image ``sudo docker commit {id} angpysha/mytfgpu:{version}``
3. Push chnages to docker repository 
``sudo docker push angpysha/mytfgpu:{version}``