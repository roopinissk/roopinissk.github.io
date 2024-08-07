---
title: I built an ML model!!! (well, sort of.) (2)
date: 2024-08-07
description: Learning Pytorch
authors: ["roopini"]
tags:
  - #Pytorch
---
 Continued from my previous blog

### Loss function
To make better predictions, we need to know how good or bad our model is performing. Loss function does exactly that. Based on the prediction, we compare it to the estimated value and check how much loss has happened in predicting right. This can be done using the function `loss = nn.MSELoss()`. MSE is mean squared error which makes the difference in the loss by squaring them

Next, comes the optimizer. With a loss function, we can tell how well (or poorly) our neural network is performing. To improve on our model’s performance, we need to adjust the weights and biases (Read my linear regression blog understand weights better). This is what the optimizer algorithm does. There are many different optimization algorithms. One of the most common is called gradient descent. 

`import torch.optim as optim`
`optimizer = optim.Adam(model.parameters(), lr=0.01)`

- `model.parameters()` tells Adam what our current weights and biases are
- `lr=0.01` tells Adam to set the learning rate to `0.01`

### Training 
To optimize our model, we have to go back and make small adjustment of weights to arrive at a more accurate prediction. This is where back propogation is applied using the function `MSE.backward()` so optimizer is applied during the back propogation

``` python 
predictions = model(X) # forward pass
MSE = loss(predictions,y) # compute loss
MSE.backward() # compute gradients
optimizer.step() # update weights and biases
```
This code block is usually made into a training loop which will perform multiple optimizations which is basically an attempt to reduce loss. The training loop or `epoch` is set to the desired number 0 to 1000 or even more. So, for example if the epoch is set to 1000, the entire process of changing weights and optimization is done 1000 times. This determines the prediction accuracy of the model.

``` python
num_epochs = 1000
for epoch in range(num_epochs):
    predictions = model(X) # forward pass
    MSE = loss(predictions,y) # compute loss
    MSE.backward() # compute gradients
    optimizer.step() # update weights and biases
    optimizer.zero_grad() # reset the gradients for the next iteration
```

### Testing
Testing is only done on a part of the data. The original dataset is usually split into training and testing data. Its usually a 80% to 20% split. This is done with the help of the libraries such as tensor flow, pytorch or scikit-learn. An example using sklearn below

``` python 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,
    train_size=0.80,
    test_size=0.20,)
``` 

X is input (X - capitalized as general accepted convention in math)
y is output

- train data: X_train , y_train
- test data: X_test, y_test

### Model Evaluation
The model is evaluated using the test data using the following syntax
``` python
model.eval()
with torch.no_grad():
    predictions = model(X_test)
    test_MSE = loss(predictions, y_test)
``` 

`model.eval()` function evaluates the model
`torch.no_grad()` removes gradient calculations (not done outside training) 

### Saving and loading model
Once your model is ready, you can save it and load it so that you dont have to train it again and you can preserve its learned parameters. Also better reproducibility, you can share the model with any one adn multiple other uses. 

``` python
torch.save(model, 'model.pth')
loaded_model = torch.load('model.pth')
``` 

'model.pth' - saves the model to a specific path and loads it from that saved path. 
