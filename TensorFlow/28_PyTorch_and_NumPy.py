import torch
import numpy as np

print(f'PyTorch version: {torch.__version__}\n')

print('PyTorch tensors and NumPy')
print('Data in NumPy, want in PyTorch tensor -> torch.from_numpy(ndarray)\n'
      'PyTorch tensor -> NumPy -> torch.Tensor.numpy()')

print('-------------------------------------------------------------------')
print('NumPy array to tensor')

array_x = np.arange(1.0, 8.0)
tensor_x = torch.from_numpy(array_x)

print(f'array_x: {array_x}')
print(f'array_x.dtype: {array_x.dtype}')
print(f'tensor_x: {tensor_x}')
tensor32 = torch.from_numpy(array_x).type(torch.float32)
print(f'WARNING _ When converting from numpy -> pytorch, pytorch reflects numpy\'s default datatype of float64 unless specified otherwise\n'
      'We have to convert datatype from float64 to float 32\n'
      f'eg: tensor32 = torch.from_numpy(array_x).type(): {tensor32} , datatype: {tensor32.dtype}\n')

print('Change the value of array_x, what will this do to \'tensor_x\'')
array_x = array_x + 1
print(f'array_x = array_x + 1:\n{array_x}')
print(f'tensor_x:\n{tensor_x}')
print('-------------------------------------------------------------------')
print('Tensor to NumPy array')
tensor_y = torch.ones(7)
numpy_from_tensor = torch.Tensor.numpy(tensor_y)
print(f'tensor_y:\n{tensor_y}, datatype: {tensor_y.dtype}')
print(f'numpy_from_tensor:\n{numpy_from_tensor}, datatype: {numpy_from_tensor.dtype}')
print('Change the value of tensor_y, what happens to \'numpy_from_tensor\'')
tensor_y = tensor_y + 1
print(f'tensor_y = tensor_y + 1:\n{tensor_y}')
print('numpy_from_tensor:\n', numpy_from_tensor)
