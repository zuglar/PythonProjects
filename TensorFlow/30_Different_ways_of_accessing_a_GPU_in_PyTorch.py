import torch

print(f'PyTorch version: {torch.__version__}\n')

print('Running tensors and Pytorch objects on the GPUs (and making faster computations)\n'
      'GPUs == faster computation on numbers, thanks to CUDA + NVIDIA hardware + PyTorch working behind the scene'
      'to make everything hunky dory (good)\n'
      'https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/'
      '\n')

print('-------------------------------------------------------------------')
print('Check for GPU access with PyTorch')
print(f'torch.cuda.is_available(): {torch.cuda.is_available()}\n')

if torch.cuda.is_available():
      print('CUDA is available.\n')
else:
      print('CUDA not is available.\n')

print('-------------------------------------------------------------------')

print('For PyTorch since it is capable of running compute ont GPU or CPU, it is best practice \n'
      'to setup device agnostic code:\n\n'
      'https://pytorch.org/docs/main/notes/cuda.html#best-practices\n\n'
      'E.g. run on GPU if available, else default to CPU')
print('Setup device agnostic code')
device = "cpu"
if torch.cuda.is_available():
      device = "cuda"
else:
      device = "cpu"

print(f'device: {device}\n')

print('Count number of devices')
if device == "cuda":
      print(f"Number of devices: {torch.cuda.device_count()}")


