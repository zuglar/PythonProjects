import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.matrixlib.defmatrix import matrix
from sympy import print_tree

print('PyTorch version: ', torch.__version__)

some_tensor = torch.rand([3, 4])

print('Getting information from tensors (tensor attributes)')
print('1. Tensors is not right datatype. To get datatype from a tensor, can use tensor.dtype')
print('2. Tensors is not right shape. To get shape from a tensor, can use tensor.shape')
print('3. Tensors is not right device. To get device from a tensor, can use tensor.device')
print()
print('some_tensor:', some_tensor)
print()
print(f"DataType: {some_tensor.dtype}")
print(f"Shape: {some_tensor.shape}")
print(f"Device: {some_tensor.device}")
print(f"Size: {some_tensor.size()}")