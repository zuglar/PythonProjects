import torch
import numpy as np
from torch.xpu import device

# create empty tensor
x = torch.empty(1) # 1D tensor
print("1D tensor", '\n', x, '\n')
print("- - - - - - - - - - - - - - - - - - - - - -", '\n')

x = torch.empty(3) # 1D tensor 3 elements
print("1D tensor 3 elements", '\n', x, '\n')
print("- - - - - - - - - - - - - - - - - - - - - -", '\n')

x = torch.empty(2, 3) # 2D tensor
print("2D tensor", '\n', x, '\n')
print("- - - - - - - - - - - - - - - - - - - - - -", '\n')

x = torch.empty(2, 2, 3) # 3D tensor
print("3D tensor", '\n', x, '\n')
print("- - - - - - - - - - - - - - - - - - - - - -", '\n')

# create tensor with random values
x = torch.rand(2 , 3) # 2D tensor with random values
print("2D tensor with random values", '\n', x, '\n')
print("- - - - - - - - - - - - - - - - - - - - - -", '\n')

# create tensor with zeros
x = torch.zeros(2 , 3) # 2D tensor with zeros
print("2D tensor with zeros", '\n', x, '\n')
print("- - - - - - - - - - - - - - - - - - - - - -", '\n')

# create tensor with ones
x = torch.ones(2 , 3) # 2D tensor with zeros
print("2D tensor with ones", '\n', x, '\n')
print("- - - - - - - - - - - - - - - - - - - - - -", '\n')

# create tensor with data types
x = torch.ones(3, 2, dtype=torch.int)
print("2D tensor with data type int", '\n', x.dtype, '\n')

x = torch.ones(3, 2, dtype=torch.double)
print("2D tensor with data type double", '\n', x.dtype, '\n')

x = torch.ones(3, 2, dtype=torch.float16)
print("2D tensor with data type float16", '\n', x.dtype, '\n')
print("- - - - - - - - - - - - - - - - - - - - - -", '\n')

# tensor size
x = torch.ones(3, 2, dtype=torch.int)
print("Size of tensor", '\n', x.size(), '\n')
print("- - - - - - - - - - - - - - - - - - - - - -", '\n')

# create tensor with elements
x = torch.tensor(([1.3, 2.5, 0.2], [4, 5, 6]))
print("Tensor with base elements", '\n', x, '\n')
print("- - - - - - - - - - - - - - - - - - - - - -", '\n')

# addition of two tensors
x = torch.tensor(([1, 2, 3], [4, 5, 6]), dtype=torch.int)
y = torch.tensor(([7, 8, 9], [10, 11, 12]), dtype=torch.int)
z = x + y
z1 = torch.add(x, y)
print("x tensor data", '\n', x, '\n')
print("y tensor data", '\n', y, '\n')
print("Simple addition of two tensors, z = x + y", '\n', z, '\n')
print("Simple addition of two tensors, z1 = torch.add(x, y)", '\n', z1, '\n')
y.add_(x)
print("In place addition... It will modify the \"y\" ... y.add_(x)", '\n', y, '\n')
print("- - - - - - - - - - - - - - - - - - - - - -", '\n')

# subtraction of two tensors
x = torch.tensor(([1, 2, 3], [4, 5, 6]), dtype=torch.int)
y = torch.tensor(([7, 8, 9], [10, 11, 12]), dtype=torch.int)
z = x - y
z1 = torch.sub(x, y)
print("x tensor data", '\n', x, '\n')
print("y tensor data", '\n', y, '\n')
print("Simple subtraction of two tensors, z = x - y", '\n', z, '\n')
print("Simple subtraction of two tensors, z1 = torch.sub(x, y)", '\n', z1, '\n')
y.sub_(x)
print("In place addition... It will modify the \"y\" ... y.sub_(x)", '\n', y, '\n')
print("- - - - - - - - - - - - - - - - - - - - - -", '\n')

# multiplication of two tensors
x = torch.tensor(([1, 2, 3], [4, 5, 6]), dtype=torch.int)
y = torch.tensor(([7, 8, 9], [10, 11, 12]), dtype=torch.int)
z = x * y
z1 = torch.mul(x, y)
print("x tensor data", '\n', x, '\n')
print("y tensor data", '\n', y, '\n')
print("Simple multiplication of two tensors, z = x * y", '\n', z, '\n')
print("Simple multiplication of two tensors, z1 = torch.mul(x, y)", '\n', z1, '\n')
y.mul_(x)
print("In place multiplication... It will modify the \"y\" ... y.mul_(x)", '\n', y, '\n')
print("- - - - - - - - - - - - - - - - - - - - - -", '\n')

# division of two tensors
x = torch.tensor(([1, 2, 3], [4, 5, 6]), dtype=torch.double)
y = torch.tensor(([7, 8, 9], [10, 11, 12]), dtype=torch.double)
z = x / y
z1 = torch.div(x, y)
print("x tensor data", '\n', x, '\n')
print("y tensor data", '\n', y, '\n')
print("Simple division of two tensors, z = x * y", '\n', z, '\n')
print("Simple division of two tensors, z1 = torch.div(x, y)", '\n', z1, '\n')
y.div_(x)
print("In place division... It will modify the \"y\" ... y.div_(x)", '\n', y, '\n')
print("- - - - - - - - - - - - - - - - - - - - - -", '\n')

# slice of tensor
x = torch.randint(10, (5, 3))
print("x tensor data", '\n', x, '\n')
print("Slice of tensor. x[1, :] - Row number one, all columns", '\n', x[1, :], '\n')
print("Slice of tensor. x[1, 1] - Row and column number one", '\n', x[1, 1], '\n')
print("Slice of tensor. x[:, 1] - All ow and column number one", '\n', x[:, 1], '\n')
print("- - - - - - - - - - - - - - - - - - - - - -", '\n')

# reshape tensor
x = torch.randint(20, (4, 4))
print("x tensor data", '\n', x, '\n')
y = x.view(16)
print("Reshape tensor x to 1D tensor. y = x.view(16)", '\n', y, '\n')
y = x.view(-1, 8)
print("Reshape tensor x. y = x.view(-1, 8))", '\n', y, '\n')
print(y.size(), '\n')
print("- - - - - - - - - - - - - - - - - - - - - -", '\n')

# converting from numpy to torch tensor and vice versa
x = torch.ones(5)
print("x tensor data", '\n', x, '\n')
y = x.numpy()
print("Convert x tensor to numpy array. y = x.numpy()", '\n', y, '\n', type(y), '\n')

print("If the tensor on CPU not on GPU, the both objects x and y share the same memory location.")
print("If we change one object the second will be changed too !!!", '\n')

x.add_(1)
print("x tensor data", '\n', x, '\n')
print("y numpy array data", '\n', y, '\n')

x = np.ones(6)
print("x numpy array data", '\n', x, '\n')
y = torch.from_numpy(x)
print("Convert x numpy array to tensor y. y = torch.from_numpy(x)", '\n', y, '\n', type(y), '\n')

print("If the tensor on CPU not on GPU, the both objects x and y share the same memory location.")
print("If we change the x numpy array data the tensor data will be changed too !!!")
x += 1
print("x numpy array data", '\n', x, '\n', type(x), '\n')
print("y tensor data", '\n', y, '\n', type(y), '\n')
print("- - - - - - - - - - - - - - - - - - - - - -", '\n')

print("Example for using CUDA !!!", '\n')

if torch.cuda.is_available():
    device = torch.device("cuda")

# creating tensor and put it on GPU
x = torch.ones(5, device=device)
# creating simple tensor on CPU and move it to GPU
y = torch.ones(5)
y = y.to(device)
z = x + y
print("x tensor data", '\n', x, '\n')
print("y tensor data", '\n', y, '\n')
print("z = x + y", '\n', z, '\n')

x.add_(10)
z = x + y
print("x tensor data modified", '\n', x, '\n')
print("y tensor data", '\n', y, '\n')
print("z = x + y", '\n', z, '\n')

print("z is on GPU and the converting it to numpy array is not possible.")
print("Therefore we have to put the z tensor to CPU and convert it to numpy array")
z = z.to("cpu")
z1 = z.numpy()
print("z1 numpy array data", '\n', z1, '\n', type(z1))
print("- - - - - - - - - - - - - - - - - - - - - -", '\n')