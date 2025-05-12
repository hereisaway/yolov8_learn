import torch

# 检查 CUDA 是否可用
cuda_available = torch.cuda.is_available()
print("CUDA 可用:", cuda_available)

# 检查当前 PyTorch 版本
print("PyTorch 版本:", torch.__version__)

# 如果 CUDA 可用，打印设备数量和名称
if cuda_available:
    print("CUDA 设备数量:", torch.cuda.device_count())
    for i in range(torch.cuda.device_count()):
        print(f"设备 {i}: {torch.cuda.get_device_name(i)}")
else:
    print("当前安装的 PyTorch 是 CPU 版本。")