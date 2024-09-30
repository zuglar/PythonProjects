import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.src.ops import dtype
from numpy.matrixlib.defmatrix import matrix
from sympy import print_tree
from triton.language import tensor

print('PyTorch version: ', torch.__version__)

# Float 32 tensor
float_32_tensor = torch.tensor([3.0, 6.0, 9.0], dtype=None)

print("float_32_tensor: ", float_32_tensor)
print('float_32_tensor.dtype: ', float_32_tensor.dtype)
print('DEFAULT  Datatype is FLOAT32')
print('-------------------------------------------------------------------')

# Float 16 tensor
float_16_tensor = torch.tensor([3.0, 6.0, 9.0], dtype=torch.float16)
print("float_16_tensor: ", float_16_tensor)
print('float_16_tensor.dtype: ', float_16_tensor.dtype)

# Create tensor with the three of the most important parameters
print('Create tensor with the three of the most important parameters:')
print('- dtype; What datatype is the tensor (e.g. float16, float32, bool ... read the documentation)')
print('- device; What device is your tensor on')
print('- requires_grad; whether or not to track gradients with this tensors operation')
print()
print('Tensor datatypes is one of the 3 big errors you will run into with PyTorch and DL:')
print('1. Tensors is not right datatype. To get datatype from a tensor, can use tensor.dtype')
print('2. Tensors is not right shape. To get shape from a tensor, can use tensor.shape')
print('3. Tensors is not right device. To get device from a tensor, can use tensor.device')
print('-------------------------------------------------------------------')
print('Change the datatype of tensor:')
print('float_16_tensor.dtype: ', float_16_tensor)

float_16_tensor = torch.float64
print('float_16_tensor.dtype: ', float_16_tensor)
float_16_tensor = torch.float16
print('float_16_tensor.dtype: ', float_16_tensor)
print('-------------------------------------------------------------------')

float_16_tensor = torch.tensor([3.0, 6.0, 9.0], dtype=torch.float16)
print("float_16_tensor: ", float_16_tensor)
print("float_32_tensor: ", float_32_tensor)


print('Multiply: float_16_tensor * float_32_tensor : ', float_16_tensor * float_32_tensor)
print()
int_32_tensor = torch.tensor([3, 6, 9], dtype=torch.int32)
print('int_31_tensor: ', int_32_tensor)
print('Multiply: int_32_tensor * float_32_tensor : ', int_32_tensor * float_32_tensor)