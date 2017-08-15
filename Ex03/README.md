# Exercise 03
For "Neural Networks and Genetic Programming" course

### Instructions 
1. Implement a sigmoid neuron. 
2. Can a sigmoid neuron represent AND, OR, NAND logical gates?
3. Can a sigmoid neuron be used for learning the 2D point location example? What are the difference in terms of learning (i.e., how does the sigmoid neuron
behaves with the perceptron learning algorithm)? 

### Implementation of sigmoid neuron
It's very similar to the Perceptron, but the 'operate' function is different. It uses the Sigmoid Function.

### Implementation of logical gates
A neuron can be used to represent AND, OR, NAND logical gates! But we have to modify the weights, bias and threshold :B
Tests for implemented logical gates can be found in GatesTests.py.

### Learning neuron
Implementation of a learning neuron that classifies points (x, y) with colours red & blue according to their position (above or below) relative to a determined line.

In this implementation the line is defined by random values (in the range [-5, 5]) of m, the slope of the line, and random values (in the range [-25, 25]) of n, the y-intercept of the line. The points are limited to a range of [-50, 50] in both axis.

The perceptron trains 10000 times, comparing its calculated output with the desired output and updating its weights accordingly. After the training we can test it by classifying 300 points and plotting them. 

We can observe that with the defined initial weights (1), bias (0.5) and c (0.02) , the perceptron tends to not work so well for certain lines, in particular when the slope is in the range (-1, 0), but for other cases it works pretty well. 

### How to run
- Run Main.py to train perceptron and see the results for trained perceptron for a random line.
