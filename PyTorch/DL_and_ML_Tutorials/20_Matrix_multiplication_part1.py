import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.matrixlib.defmatrix import matrix
from sympy import print_tree

print(f'PyTorch version: {torch.__version__}\n')

tensor = torch.tensor([1, 2, 3])

print('Two main ways of performing multiplication in neural networks and deep learning:')
print('* * * * * * * * * * * * Element-wise multiplication')
print('tensor * tensor')
print(tensor, ' * ', tensor, ' = ', tensor * tensor)
print()
print('* * * * * * * * * * * * Matrix multiplication (dot product)')
print('torch.matmul(tensor, tensor): ', torch.matmul(tensor, tensor))

print()
print('One of the most common errors in deep learning: SHAPE ERRORS')
print()
print('There are two main rules that performing matrix multiplication needs to satisfy:')
print('1. The INNER DIMENSIONS must much:\n'
      '   - (3, 2) @ (3, 2) will  not work\n'
      '   - (2, 3) @ (3, 2) will work\n'
      '   - (3, 2) @ (2, 3) will work\n'
      '2. The resulting matrix has the shape of outer dimensions:\n'
      '   - (2, 3) @ (3, 2) -> (2, 2)\n'
      '   - (3, 2) @ (2, 3) -> (3, 3)')

print('Shapes for matrix multiplication')
tensor_A = torch.tensor([[1, 2],
                         [3, 4],
                         [5, 6]])

tensor_B = torch.tensor([[7, 10],
                         [8, 11],
                         [9, 12]])

#torch.mm(tensor_A, tensor_B) # torch.mm is the same as torch.matmul
'''
torch.matmul(tensor_A, tensor_B)
RuntimeError: mat1 and mat2 shapes cannot be multiplied (3x2 and 3x2)
'''

print('-------------------------------------------------------------------')
print('To fix our tensor shape issues, we can manipulate the shape of our tensors using a *** transpose ***')
print('A *** transpose *** switches the axes or dimensions of a given tensor')

print('tensor_B before transpose:')
print(tensor_B, tensor_B.shape)
print('tensor_B after transpose:')
print(tensor_B.T, tensor_B.T.shape)

print('torch.matmul(tensor_A, tensor_B.T):\n', torch.matmul(tensor_A, tensor_B.T))
print(f'torch.matmul(tensor_A, tensor_B.T).shape: {torch.matmul(tensor_A, tensor_B.T).shape}\n')

print('torch.matmul(tensor_A.T, tensor_B):\n', torch.matmul(tensor_A.T, tensor_B))
print(f'torch.matmul(tensor_A.T, tensor_B).shape: {torch.matmul(tensor_A.T, tensor_B).shape}\n')
print('-------------------------------------------------------------------')

print('Finding the min, max, mean, sum, etc (tensor aggregation)\n')

# Create a tensor
tensor_x = torch.arange(0, 100, 10)
print(tensor_x)
print(f'Find the min - torch.min(tensor_x): {torch.min(tensor_x)} -  tensor_x.min: {tensor_x.min()}\n')

print(f'Find the max - torch.max(tensor_x): {torch.max(tensor_x)} -  tensor_x.max: {tensor_x.max()}\n')

print(f'Find the mean - torch.mean(tensor_x): {torch.mean(tensor_x.type(torch.float32))} -  tensor_x.mean: {tensor_x.type(torch.float32).mean()}')
print('!!! The *** torch.mean *** function requires a tensor of float64 datatype to work. !!!\n')

print(f'Find the sum - torch.sum(tensor_x): {torch.sum(tensor_x)} -  tensor_x.sum: {tensor_x.sum()}')
print('-------------------------------------------------------------------')
print('Finding the positional of min and max')
print('Finding the position in tensor that has the minimum value with argmin() -> returns the index position of target tensor where the minimum value occurs.')

tensor_x = torch.arange(1, 100, 10)
print(f'tensor_x:\n{tensor_x}')
print(f'tensor_x.argmin() - index value: {tensor_x.argmin()}')
print(f'tensor_x value at index {tensor_x.argmin()} is {tensor_x[tensor_x.argmin()]}\n')

print('Finding the position in tensor that has the maximum value with argmax() -> returns the index position of target tensor where the maximum value occurs.')
print(f'tensor_x.argmin() - index value: {tensor_x.argmax()}')
print(f'tensor_x value at index {tensor_x.argmax()} is {tensor_x[tensor_x.argmax()]}\n')