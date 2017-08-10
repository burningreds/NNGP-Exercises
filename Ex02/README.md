# Exercise 02
For "Neural Networks and Genetic Programming" course

Implementation of a learning perceptron that classifies points (x, y) with colours red & blue according to their position (above or below) relative to a determined line.

In this implementation the line is defined by random values (in the range [-5, 5]) of m, the slope of the line, and random values (in the range [-25, 25]) of n, the y-intercept of the line. The points are limited to a range of [-50, 50] in both axis.

The perceptron trains 10000 times, comparing its calculated output with the desired output and updating its weights accordingly. After the training we can test it by classifying 300 points and plotting them. 

We can observe that with the defined initial weights (1), bias (0.5) and c (0.02) , the perceptron tends to not work so well for certain lines, in particular when the slope is in the range (-1, 0), but for other cases it works pretty well. 

### How to run
- Run Main.py to train perceptron and see the results for trained perceptron for a random line.
