---
title: Understanding Neural Networks. Sort of. 
date: 2024-07-24
description: My attempt at learning ML 
authors: ["roopini"]
tags:
  - Neural Networks
  - Linear regression
---

As a part of my part of my python programming course I have an assignment. I can pick a python library of my choice and give a demo. (Its a group project involving 3 people)

We chose PyTorch as our library of interest. I have been reading since yesterday about PyTorch. Codecademy is a super great resource that I found online. I've been using it a little over a year now and its amazing. For someone who knows nothing about programming, its a great place to start. 

I took this really short course on codecademy on PyTorch and neural networks. Here's what I learned. 

A neural network has an input layer and an output layer (may have mutliple layers in between). To understand how data flows within the networks its useful to understand what linear regression is. 

Linear regression: 
Lets say someone you know wants to move in to your city and is seeking your help to rent a apartment. Irrespective of which place they want to stay in, your mind has a vague idea of how much the rent would be based on the locality. From living in the city all your life, your mind has stored details such as railway lines, bus depots, shopping malls, company spcaes and what not. Now, based on these details you would be able to sort of predict what the rent might be in a particular place. Because your mind is trained by observing these different data points from the city. 

Lets take an example, lets look at Chennai, if you would like to suggest your friend to stay at a studio in  Madipakkam, the rent is going to be quite affordable lets say INR 10,000, the place is well connected to all railway lines etc. However, when you look at the price of the same studio in Nungambakkam, the stay is going to be expensive INR 20,000 (twice as much!) because of how well connected and within the city the place is. Now you are a person who is not a realtor and ofcourse these numbers might not be accurate however, in your mind you were able to adjust the price because of other details of the place. Now this adjustment is what is called as "weights". For each input fed into the neural network, the model adds weights to adjust the value of the input (based on training knowledge) and gives a predicted output. 
