import torch

print(f'PyTorch version: {torch.__version__}\n')
print('PyTorch reproducibility (talking the random out of random)\n')
print('In sort how neural network learns:\n'
      'start with random numbers perform (->) tensor operation -> update random numbers to try and make better\n'
      'representations of data -> again -> again -> again -> again -> ...\n')
print('To reduce the randomness in neural networks and PyTorch comes the concept of a ***random seed***\n'
      'Essentially what the random seed does is \"flavour\" the randomness\n')
print('-------------------------------------------------------------------')
print('Create to random tensors')
random_tensor_A = torch.rand(3, 4)
random_tensor_B = torch.rand(3, 4)
print(f'random_tensor_A:\n{random_tensor_A}')
print(f'random_tensor_B:\n{random_tensor_B}')
print(f'random_tensor_A == random_tensor_B :\n{random_tensor_A == random_tensor_B}\n')
print('-------------------------------------------------------------------')
print('Let\'s make some random but reproducible tensors\n'
      'Set the random seed')
RANDOM_SEED = 42
print('Start - random seed')
torch.manual_seed(RANDOM_SEED)
random_tensor_C = torch.rand(3, 4)
print('End - random seed')
print('torch.manual_seed(RANDOM_SEED) - it only works for one block of code ')
torch.manual_seed(RANDOM_SEED)
random_tensor_D = torch.rand(3, 4)

print(f'random_tensor_C:\n{random_tensor_C}')
print(f'random_tensor_D:\n{random_tensor_D}')
print(f'random_tensor_C == random_tensor_D :\n{random_tensor_C == random_tensor_D}\n')

print('Extra resources for reproducibility:\n'
      'https://pytorch.org/docs/stable/notes/randomness.html\n'
      'https://en.wikipedia.org/wiki/Random_seed')