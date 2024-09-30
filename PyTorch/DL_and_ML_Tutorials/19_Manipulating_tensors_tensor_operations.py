import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.matrixlib.defmatrix import matrix
from sympy import print_tree

print(f'PyTorch version: {torch.__version__}\n')

tensor = torch.tensor([1, 2, 3])

print('Tensor operation include:')
print('* * * * * * * * * * * * Addition')
print('tensor + 10: ', tensor + 10 )
print('torch.add(tensor,10): ', torch.add(tensor,10))
print('* * * * * * * * * * * * Subtraction')
print('tensor - 10: ', tensor - 10 )
print('torch.sub(tensor,10): ', torch.sub(tensor,10))
print('* * * * * * * * * * * * Multiplication (element-wise)')
print('tensor * 10: ', tensor *  10 )
print('torch.mul(tensor, 10): ', torch.mul(tensor, 10))
print('* * * * * * * * * * * * Division')
print('tensor / 10: ', tensor /  10 )
print('torch.div(tensor, 10): ', torch.div(tensor, 10))
print('* * * * * * * * * * * * Matrix multiplication')
