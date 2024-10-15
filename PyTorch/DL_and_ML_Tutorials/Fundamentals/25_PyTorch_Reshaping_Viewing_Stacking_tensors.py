import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.ma.core import squeeze
from numpy.matrixlib.defmatrix import matrix
from sympy import print_tree

print(f'PyTorch version: {torch.__version__}\n')

print('Reshaping, stacking, squeezing and unsqueezing tensors\n'
      '* Reshaping - reshapes an input tensor to a defined shape\n'
      '* View - Return a view of an input tensor of certain shape but keep the same memory as the original tensor\n'
      '* Stacking - combine multiple tensors on top of each other (vstack - vertical stack) or side by side (hstack - horizontal stack)\n'
      '* Squeeze - remove all \'1\' dimensions from a tensor\n'
      '* Unsqueeze - add a \'1\' dimensions to a target tensor\n'
      '* Permute - Return a view of the input with dimensions permuted (swapped) in a certain way')
tensor_x = torch.arange(1., 10.)
print(f'tensor_x:\n{tensor_x}\nShape:\n{tensor_x.shape}\n')
print('-------------------------------------------------------------------')
print('Reshape\n'
      'Add an extra dimension')
'''
ERROR !!!!!
tensor_x_reshaped = tensor_x.reshape(1, 7)
print(f'tensor_x_reshaped.\n{tensor_x_reshaped}\nShape:\n{tensor_x_reshaped.shape}\n')
'''

tensor_x_reshaped_1 = tensor_x.reshape(1, 9)
print(f'tensor_x_reshaped_1.\n{tensor_x_reshaped_1}\nShape:\n{tensor_x_reshaped_1.shape}\n')

tensor_x_reshaped_2 = tensor_x.reshape(9, 1)
print(f'tensor_x_reshaped_2.\n{tensor_x_reshaped_2}\nShape:\n{tensor_x_reshaped_2.shape}\n')
print('-------------------------------------------------------------------')

tensor_x = torch.arange(1., 13.)
tensor_x_reshaped_3 = tensor_x.reshape(3, 4)
print(f'tensor_x_reshaped_3.\n{tensor_x_reshaped_3}\nShape:\n{tensor_x_reshaped_3.shape}\n')

print('-------------------------------------------------------------------')
print("Change the view")
tensor_x = torch.arange(1., 10.)
print(f'tensor_x:\n{tensor_x}\nShape:\n{tensor_x.shape}\n')

tensor_x_reshaped_1 = tensor_x.reshape(1, 9)
print(f'tensor_x_reshaped_1.\n{tensor_x_reshaped_1}\nShape:\n{tensor_x_reshaped_1.shape}\n')

tensor_z = tensor_x.view(1, 9)
print(f'tensor_z:\n{tensor_z}\nShape:\n{tensor_z.shape}\n')

print('Changing tensor_z changes tensor_x (because a view a tensor shares the same memory as the original input)')
print('Changing the first element of tensor_z the first element of tensor_x will be changed')

tensor_z[:, 0] = 5
print(f'tensor_z:\n{tensor_z}\ntensor_x:\n{tensor_x}\n')

print('-------------------------------------------------------------------')
print('Stack tensors on top of each other (vstack - vertical stack)')

tensor_x_stacked = torch.stack([tensor_x, tensor_x, tensor_x, tensor_x], dim=0)
print(f'tensor_x_stacked - dim=0\n{tensor_x_stacked}\n')

tensor_x_stacked = torch.stack([tensor_x, tensor_x, tensor_x, tensor_x], dim=1)
print(f'tensor_x_stacked , dim=1:\n{tensor_x_stacked}\n')

print('torch.hstack: https://pytorch.org/docs/stable/generated/torch.hstack.html\n'
      'torch.vstack: https://pytorch.org/docs/stable/generated/torch.vstack.html\n')

print('-------------------------------------------------------------------')
print('Squeeze\n'
      'torch.squeeze() - removes all single dimensions from a target tensor\n')
print(f'Previous tensor_x_reshaped_1:\n{tensor_x_reshaped_1}\n'
      f'Previous shape:\n{tensor_x_reshaped_1.shape}\n'
      f'Remove extra dimension from tensor_x_reshaped_1.')
tensor_x_squeezed = tensor_x_reshaped_1.squeeze()

print(f'New tensor_x_squeezed:\n{tensor_x_squeezed}\n'
      f'New shape:\n{tensor_x_squeezed.shape}')

print('-------------------------------------------------------------------')
print('Unsqueeze\n'
      'torch.unsqueeze() - adds  a single dimensions to a target tensor at a specific dim (dimension)\n')
print(f'Previous tensor_x_squeezed:\n{tensor_x_squeezed}\n'
      f'Previous shape:\n{tensor_x_squeezed.shape}\n'
      f'Add extra dimension with unsqueeze')
tensor_x_unsqueezed = tensor_x_squeezed.unsqueeze(dim=0)
print(f'New tensor_x_unsqueezed:\n{tensor_x_unsqueezed}\n'
      f'New shape:\n{tensor_x_unsqueezed.shape}')

print('-------------------------------------------------------------------')
print('Permute\n'
       'torch.permute - rearranges  the dimensions of a target tensor in a specified order')
# work with images
x_original = torch.rand(size=(224, 244, 3)) # [height, width, colour_channels]
print(f'Original shape: {x_original.shape}')
print('Permute the x_original tensor to rearrange the axis (or dim) order, shift axis 0-> 1, 1->2, 2->0')
x_permuted = x_original.permute(2, 0, 1) # [colour_channels, height, width]
print(f'Permuted shape: {x_permuted.shape}')

print('-------------------------------------------------------------------')
print('Indexing (selecting data from tensors)\n'
      'Indexing with PyTorch is similar to indexing with NumPy.')

x_tensor = torch.arange(1, 10).reshape(1, 3, 3)
print(f'x_tensor:\n{x_tensor}\nshape:\n{x_tensor.shape}')
print('Let\'s index on our new tensor' )
print(f'x_tensor[0]:\n{x_tensor[0]}')
print('Let\'s index on the middle bracket (dim=1)' )
print(f'x_tensor[0][0]:\n{x_tensor[0][0]}')
print('or')
print(f'x_tensor[0, 0]:\n{x_tensor[0, 0]}')
print('Let\'s index on the most inner bracket (last dimension)' )
print(f'x_tensor[0][0][0]:\n{x_tensor[0][0][0]}')
# print(f'x_tensor[1][1][1]:\n{x_tensor[1][1][1]}') # error
print(f'x_tensor[0][1][1]:\n{x_tensor[0][1][1]}') # number 5
print(f'x_tensor[0][2][2]:\n{x_tensor[0][2][2]}') # number 9
print('You can also use ":" to select "all" of a target dimension')
print(f'x_tensor[:, 0]:\n{x_tensor[:, 0]}')
print(f'x_tensor[:, 2]:\n{x_tensor[:, 2]}')
print('Get all values of 0th and 1st dimension but only index 1 of 2nd dimension')
print(f'x_tensor[:, :, 1]:\n{x_tensor[:, :, 1]}')
print("Index on tensor_x to return 3, 6, 9")
print(f'x_tensor[:, :, 2]:\n{x_tensor[:, :, 2]}')
print("Index on tensor_x to return 2, 5, 8")
print(f'x_tensor[:, :, 2]:\n{x_tensor[:, :, 1]}')
print("Index on tensor_x to return 9")
print(f'x_tensor[:, :, 2]:\n{x_tensor[0, 2, 2]}')
print('or')
print(f'x_tensor[0][2][2]:\n{x_tensor[0][2][2]}')