import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.ma.core import squeeze
from numpy.matrixlib.defmatrix import matrix
from sympy import print_tree

print(f'PyTorch version: {torch.__version__}\n')

print('PyTorch tensors and NumPy\n'
      'NumPy is a popular scientific Python numerical computing library.\n'
      'And because of this, PyTorc has functionality to interact with it.\n'
      '* Data in NumPy, want in PyTorch tensor ->  torch.from_numpy(ndarray)\n'
      '* PyTorch tensor->Numpy-> torch.Tensor.numpy()\n\n')

print('NumPy array to tensor')

