'''
what_were_covering = {1: "data (prepare and load)",
    2: "build model",
    3: "fitting the model to data (training)",
    4: "making predictions and evaluating a model (inference)",
    5: "saving and loading a model",
    6: "putting it all together"
}
'''
from typing import Union, Callable, Tuple, Any, Optional, Dict

import torch
from torch import nn # nn contains all of PyTorch's building blocks for neural networks
import matplotlib.pyplot as plt
from torch.nn.modules.module import T
from torch.utils.hooks import RemovableHandle

# Check PyTorch version
print(torch.__version__)
print()
print('Data (preparing and loading)\n')
print('Machine learning is a game of two parts:\n'
      '1. Turn your data, whatever it is, into numbers (a representation).\n'
      '2. Pick or build a model to learn the representation as best as possible.\n')
print('Let\'s create some know data using the linear regression formula (Y = a + bx).\n'
      'We will use linear regression formula to make a straight line with know parameters.\n\n')

print('Create known parameters weight and bias\n')
weight = 0.7    # from the linear regression formula it is 'b'
bias = 0.3      # from the linear regression formula it is 'a'

print('Create data, range of numbers\n')
start = 0
end = 1
step = 0.02

X = torch.arange(start, end, step).unsqueeze(dim=1)

# the linear regression formula (Y = a + bx)

y = bias + weight * X

print(f'X:\n{X[:10]}\ny:\n{y[:10]}\n')

print(f'len(X): {len(X)}, len(y): {len(y)}\n\n')

print('36. Splitting our data into training and test sets (one of the most\n'
      '     important concepts in machine learning in general\n')
print('Let\'s create a training and set with our data\n')
print('Create a train/test split\n')

train_split = int(0.8 * len(X))     # 80% of total data
X_train, y_train = X[: train_split], y[:train_split]
X_test, y_test = X[train_split:], y[train_split:]

print(f'X_train: {len(X_train)}, y_train: {len(X_train)}\n'
      f'X_test: {len(X_test)}, y_test: {len(y_test)}\n\n')

print('37. Building a function to visualize our data\n')

def plot_predictions(train_data = X_train, train_labels = y_train, test_data = X_test, test_labels = y_test, predictions = None):
      '''
      Plots training data, test data and compare predictions
      '''

      plt.figure(figsize=(10, 7))

      # Plot training data in blue
      plt.scatter(train_data, train_labels, c="b", s=4, label="Training data")

      # Plot test data in green
      plt.scatter(test_data, test_labels, c="g", s=4, label="Testing data")

      if predictions is not None:
            # Plot the predictions in red (predictions were made on the test data)
            plt.scatter(test_data, predictions, c="r", s=4, label="Predictions")

      # Show the legend
      plt.legend(prop={"size": 14})
      plt.show()


plot_predictions()

print()
print('38. Creating our first PyTorch model for linear regression\n\n')

print('Create linear regression model class.\n')

print('What our model does:\n'
      '* Start with random values (weight and bias)\n'
      '* Look at training data and adjust the random values to better represent (or get closer to) ideal values\n'
      '  (the weight and bias values we used to create  the data)\n\n')

print('How does it do so?\n'
      '1. Gradient descent\n' # https://www.youtube.com/watch?v=IHZwWFHWa-w&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&index=2
      '2. Backpropagation\n') # https://www.youtube.com/watch?v=Ilg3gGewQ5U


class LinearRegressionModel(nn.Module): # <- almost everything in PyTorch inherits from nn.Module
      # constructor
      def __init__(self):
            super().__init__()
            # Initialize model parameters
            self.weights = nn.Parameter(torch.randn(1,                  # <- Start with random weight and try to adjust it to the ideal weight
                                                    requires_grad=True, # <- can this parameter be updated via gradient descent?
                                                    dtype=torch.float)) # PyTorch loves the datatype torch.float32

            self.bias = nn.Parameter(torch.randn(1,                     # <- Start with random bias and try to adjust it to the ideal weight
                                                 requires_grad=True,    # <- can this parameter be updated via gradient descent?
                                                 dtype=torch.float))    # PyTorch loves the datatype torch.float32

      # Forward method to define computation in the model
      def forward(self, x: torch.Tensor) -> torch.Tensor:   # "x" is the input data
            return self.weights * x + self.bias  # this is the linear regression formula

print('39. Breaking down what is happening in our PyTorch linear regression model\n')

print('40. Discussing some of the most important PyTorch model building classes\n')

print('PyTorch model building essentials:\n'
      '* torch.nn - contains all of the buildings for computational graphs (a neural network can be  considered o computational\n'
      '* torch.nn.Parameter - what parameters should our model try and learn, often a PyTorch layer from torch.nn  will set these for us\n'
      '* torch.nn.Module - the base class for all neural network module, if you subclass it, you should overwrite forward() method\n'
      '* torch.optim - this is where the optimizers in PyTorch live, they will help with gradient descent\n'
      '* def forward() -  All nn.Module subclasses require you to overwrite forward(), this method defines what happens in the forward computation\n\n'
      'PyTorch Cheat Sheet: https://pytorch.org/tutorials/beginner/ptcheat.html\n')

print('41. Checking out the internals of our PyTorch model\n\n')
print('Checking the contents of our PyTorch model\n'
      'Now we have created a model, let\'s see what is inside...\n'
      'So we can check our model parameters or what is inside our model using ... parameters()\n\n')

print('Create a random seed\n'
      'torch.manual_seed(42)\n')
torch.manual_seed(42)

print('Create an instance of the model(this is a subclass of nn.Model\n'
      'model_0 = LinearRegressionModel()\n')
model_0 = LinearRegressionModel()
print('model_0 is instance of ', model_0, '\n')

print('Parameters of model_0:\n', list(model_0.parameters()), '\n')

print('List name parameters (dictionary of the parameters of our model):\n', model_0.state_dict(), '\n')

print('42. Making predictions with our random model using torch.inference_mode()\n\n'
      'To check our model\'s predictive power, let\'s see how well it predicts y_test based on X_test\n'
      'When we pass data through our model, it is going to run it through the forward() method\n' )

print('Make prediction with model...torch.inference_mode()\n')
y_preds = 0
with torch.inference_mode():
      y_preds = model_0(X_test)

print('You can also do something similar with.torch.no_grad(), however, torch.inference_mode() is preferred\n')
# with torch.no_grad():
#       y_preds = model_0(X_test)

print(y_preds)
plot_predictions(predictions=y_preds)

print('43. Training a model with PyTorch (intuition building)\n\n'
      'The whole idea of training is for a model to move from some unknown parameters (these maybe random)\n'
      'to some known parameters.\n'
      'On in other words from a poor representation of the data to a better representation of the data.\n'
      'One way to measure how poor or how wrong your models predictions are is to use a loss function\n'
      'NOTE: The loss function also be called cost function or criterion in different areas.\n'
      'For our case, we are going to refer to it as a loss function.\n\n'
      'Things we need to train:\n'
      'Loss function: is a function to measure how wrong your model\'s predictions are to the ideal outputs,\n'
      'lower is better.\n'
      'Optimizer: Takes into account the loss of a model and adjusts the model\'s parameters (e.g. weight& biases in our case)\n'
      'to improve the loss function.\n'
      'And specifically for PyTorch, we need:\n'
      '* A training loop\n'
      '* A testing loop\n\n')

print('44. Setting up a loss function and optimizer with PyTorch\n\n')

print('Setup a loss function\n'
      'loss_fn = nn.L1Loss()')
loss_fn = nn.L1Loss()
print('loss_fn: ', loss_fn, '\n')

print('Setup an optimizer\n')