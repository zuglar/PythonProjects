import torch
import numpy as np
from torch.xpu import device

x = torch.rand(3, requires_grad=True)
print(x)

y = x + 2
print(y)
z = y * y * 2
print(z)
z = z.mean()
print(z)

z.backward() # calculate the gradient dz / dx
print(x.grad)