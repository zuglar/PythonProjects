import torch
print(f'PyTorch version: {torch.__version__}\n')

print('31 Setting up device agnostic code and putting tensors on and off the GPU\n')
print('Setup device agnostic code')
device = "cpu"
if torch.cuda.is_available():
      device = "cuda"
else:
      device = "cpu"

print('Putting tensors (and models) on the GPU\n'
      'The reason we want our tensors/models on the GPU is because using a GPU results in faster computations.\n')

print('Create a tensor (default on CPU)')
tensor_CPU = torch.tensor([1, 2, 3])
print(f'tensor_CPU:\n{tensor_CPU} , device: {tensor_CPU.device}\n')

print('Move tensor to GPU (if available)')
tensor_on_GPU = tensor_CPU.to(device)
print(f'tensor_on_GPU:\n{tensor_on_GPU} , device: {tensor_on_GPU.device}\n')

print('-------------------------------------------------------------------')
print('If tensor is on GPU, cannot transform it to NumPy.\n'
      'To fix the GPU tensor with NumPy issue, we can first set it to the CPU.')
print('Moving tensors back to the CPU')
tensor_back_on_cpu = tensor_on_GPU.cpu().numpy()
print(f'tensor_back_on_cpu:\n{tensor_back_on_cpu}')




