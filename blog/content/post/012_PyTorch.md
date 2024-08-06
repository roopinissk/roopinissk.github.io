---
title: I built an ML model!!! (well, sort of.)
date: 2024-08-06
description: Learning Pytorch
authors: ["roopini"]
tags:
  - Pytorch
---
Building a Machine Learning model involves the following steps. 
- Define what your model will do
- Collect data
- Choose model (Should read more about this)
- Train model on your dataset
- Evaluate model
- Tune and deploy model

### Tensors
Pytorch is a python library which helps in building an ML model. 
FIrst, lets talk about tensors. Imagine a spreadsheet which contains rows and columns of data, tensors are more complex which can hold data in several dimensions. The common term used is "containers" that holds numbers in a structured way. 

Why is it important to convert data into tensors? it helps in easier computation of multi-dimentional data, it has a standardized format as they can represent image, numerical, text data in a consistent format, helpful in applying mathematical operations such as linear algebra. 

So, as a first step, you would have to convert your data into tensors. This can be done with the help of the function `torch.tensor()` which can take 2 arguments- the numerical data (np array, list) and data type (int or float) 

### Layers 
Now, you would have to choose an algorithm to run a model (I only learned about linear regression so, ill explain building a model with that). The function `nn.Sequential()` is an easier way to stack layers in a neural network. 
```python
model = nn.Sequential(
    nn.Linear(2,3),
    nn.ReLU(),
    nn.Linear(3,1)
)
```

Here, nn.Linear() applies the linear regression. The numbers enclosed in parenthesis denotes the no.of nodes, Begins with 2 input layers connects to 3 nodes in the second layer. `nn.ReLU()` (an enitre topic of its own) is an activation fucntion. Breifly, it takes number as input and gives a number as the output. This helps the model to learn faster. The above mentioned code is a simple model which has an input layer, a second layer in between (or a hidden layer) and an output layer. A model can contain n number or layers. 

--- more on my next blog. 
