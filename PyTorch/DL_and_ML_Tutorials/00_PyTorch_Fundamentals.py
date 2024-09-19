import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.matrixlib.defmatrix import matrix
from sympy import print_tree

print('PyTorch version: ', torch.__version__)

# Introduction to Tensors

# Creating tensors

# Scalar
scalar = torch.tensor(7)
print('Create Scalar Tensor... scalar = torch.tensor(7): ', scalar, '\n')
print("Attributes, details of a scalar")
print('- Dimension of Scalar Tensor: ', scalar.ndim)
print('- Shape of Scalar Tensor: ', scalar.shape)
print('- Get Scalar Tensor back as Python int: ', scalar.item())
print('-------------------------------------------------------------------')

# Vector
vector = torch.tensor([7, 7])
print('Create Vector Tensor... vector = torch.tensor([7, 7]): ', vector, '\n')
print("Attributes, details of a vector")
print('- Dimension of Vector: ', vector.ndim)
print('- Shape of Vector: ', vector.shape)
print('- Elements of Vector:\n', vector[:])
print('-------------------------------------------------------------------')

# MATRIX
MATRIX = torch.tensor([[7, 8],
                       [9, 10]])
print('Create Matrix Tensor... MATRIX = torch.tensor([[7, 8],  [9, 10]]):\n ', MATRIX, '\n')
print('- Dimension of Matrix: ', MATRIX.ndim)
print('- Shape of Matrix: ', MATRIX.shape)
print('- Elements of Matrix:\n', MATRIX[:])
print('- First row of Matrix:\n', MATRIX[0])
print('- Second row of Matrix:\n', MATRIX[1])
print('-------------------------------------------------------------------')

# TENSOR
TENSOR = torch.tensor([[[1, 2, 3],
                        [3, 6, 9],
                        [2, 4, 5]]])
print('Create Tensor...\n ', TENSOR, '\n')
print('- Dimension of Tensor: ', TENSOR.ndim)
print('- Shape of Tensor: ', TENSOR.shape)
print('- Elements of Matrix:\n', TENSOR[0])
print('-------------------------------------------------------------------')

# Create a random tensors of size/shape (3,4)
print('Create a random tensors of size/shape (3,4)')

random_tensor = torch.rand(3, 4)
print('random_tensor:\n', random_tensor)
print('- Dimension of random_tensor: ', random_tensor.ndim)

# Create a random tensor with similar shape to an image tensor ...size=(number of colour channels, height, width)
random_image_size_tensor = torch.rand(size=(3, 224, 224))   # number of colour channels (R, G, B), height, width
print('- Dimension of random_image_size_tensor: ', random_image_size_tensor.ndim)
print('- Size/Shape of random_image_size_tensor: ', random_image_size_tensor.shape)
print('-------------------------------------------------------------------')

# Create Tensors with Zeros and Ones
print('Create a tensor of all zeros.')
zeros = torch.zeros(size=(3, 4))
print('torch.zeros(size=(3, 4)):\n', zeros, '\n')

print('Create a tensor of all ones.')
ones = torch.ones(size=(4, 5))
print('ones = torch.ones(size=(4, 5)):\n', ones, '\n')
print('Data type: ', ones.dtype)
print('-------------------------------------------------------------------')

# Creating a range of tensors and tensors-like
print('Creating a range of tensors.')
range_tensor = torch.arange(0, 10)
print('torch.arange(0, 10):\n', range_tensor)
one_to_ten = torch.arange(1, 11)
print('torch.arange(1, 11):\n', one_to_ten)

print('Creating a range of tensors with step.')
range_tensor = torch.arange(start=0, end=50, step=5)
print('torch.range(start=0, end=50, step=5): ', range_tensor)

print('Creating tensors like.')
ten_zeros = torch.zeros_like(input=one_to_ten)
print('torch.zeros_like(input=one_to_ten): ', ten_zeros)