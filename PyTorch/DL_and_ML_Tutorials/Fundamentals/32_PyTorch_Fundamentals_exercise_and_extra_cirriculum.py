import torch
print(f'PyTorch version: {torch.__version__}\n\n')

# https://www.learnpytorch.io/00_pytorch_fundamentals/#extra-curriculum

print('2. Create a random tensor with shape (7, 7).')
random_tensor_A = torch.rand(7, 7)
print(f'random_tensor_A.shape:\n{random_tensor_A.shape}\n{random_tensor_A}')
print('-------------------------------------------------------------------')
print('3. Perform a matrix multiplication on the tensor from 2 with another random tensor with shape (1, 7) '
      '(hint: you may have to transpose the second tensor).')

random_tensor_B = torch.rand(1, 7)
print(f'random_tensor_B\n{random_tensor_B}')

tensor_A_x_B = random_tensor_A * random_tensor_B.T

print(f'tensor_A_x_B:\n{tensor_A_x_B}')
print('-------------------------------------------------------------------')

print('4. Set the random seed to 0 and do exercises 2 & 3 over again.')
RANDOM_SEED = 0
torch.manual_seed(RANDOM_SEED)
random_tensor_A = torch.rand(7, 7)
torch.manual_seed(RANDOM_SEED)
random_tensor_B = torch.rand(1, 7)
print(f'random_tensor_A:\n{random_tensor_A}')
print(f'random_tensor_B:\n{random_tensor_B}')

tensor_A_x_B = random_tensor_A * random_tensor_B.T

print(f'tensor_A_x_B:\n{tensor_A_x_B}')

print('-------------------------------------------------------------------')
print('5. Speaking of random seeds, we saw how to set it with torch.manual_seed() but is there a GPU equivalent\n '
      '(hint: you will need to look into the documentation for torch.cuda for this one).\n'
      'If there is, set the GPU random seed to 1234.')
RANDOM_SEED = 1234
torch.cuda.manual_seed(RANDOM_SEED)
random_tensor_A = torch.rand(7, 7)
torch.cuda.manual_seed(RANDOM_SEED)
random_tensor_B = torch.rand(1, 7)
print(f'random_tensor_A:\n{random_tensor_A}')
print(f'random_tensor_B:\n{random_tensor_B}')

tensor_A_x_B = random_tensor_A * random_tensor_B.T

print(f'tensor_A_x_B:\n{tensor_A_x_B}')


print('6. Create two random tensors of shape (2, 3) and send them both to the GPU (you\'ll need access to a GPU for this).\n'
      'Set torch.manual_seed(1234) when creating the tensors (this does not have to be the GPU random seed).\n')

RANDOM_SEED = 1234

# device agnostic code
device = "cpu"

if torch.cuda.is_available():
    print('CUDA is available')
    device = "cuda"

torch.manual_seed(RANDOM_SEED)
tensor_A = torch.rand(2, 3).to(device)
torch.manual_seed(RANDOM_SEED)
tensor_B = torch.rand(2, 3).to(device)

print(f'tensor_A:\n{tensor_A}\ntensor_A.device: {tensor_A.device}')
print(f'tensor_B:\n{tensor_B}\ntensor_B.device: {tensor_B.device}')
print('-------------------------------------------------------------------')
print('7. Perform a matrix multiplication on the tensors you created in 6 (again, you may have to adjust the shapes of one of the tensors).')

tensor_A_x_B = (tensor_A * tensor_B)

print(f'tensor_A_x_B:\n{tensor_A_x_B}\ndevice: {tensor_A_x_B.device}')
print('-------------------------------------------------------------------')
print('8. Find the maximum and minimum values of the output of 7.')
print(f"Min of tensor_A_x_B: {tensor_A_x_B.min()}")
print(f"Max of tensor_A_x_B: {tensor_A_x_B.max()}")

print('-------------------------------------------------------------------')
print('9. Find the maximum and minimum index values of the output of 7.')
print(f"Index of min of tensor_A_x_B: {tensor_A_x_B.argmin()}")
print(f"Index of max of tensor_A_x_B: {tensor_A_x_B.argmax()}")

print('-------------------------------------------------------------------')
print('10. Make a random tensor with shape (1, 1, 1, 10) and then create a new tensor with all the 1 dimensions removed to be left with\n'
      'a tensor of shape (10). Set the seed to 7 when you create it and print out the first tensor and\n'
      'it is shape as well as the second tensor and it is shape.')

RANDOM_SEED = 7
torch.manual_seed(RANDOM_SEED)
tensor_1 = torch.rand(1, 1, 1, 10)
torch.manual_seed(RANDOM_SEED)
tensor_2 = torch.rand(10)
print(f'tensor_1:\n{tensor_1}\ntensor_1.shape: {tensor_1.shape}')
print(f'tensor_2:\n{tensor_2}\ntensor_2.shape: {tensor_2.shape}')