from SigmoidNeuron import SigmoidNeuron
import numpy as np


# AndPerceptron class
# Inherits from Perceptron class with corresponding weights and bias
class AndPerceptron(SigmoidNeuron):
    def __init__(self):
        self.w1 = 0.5
        self.w2 = 0.5
        self.bias = - 0.5
        self.threshold = 0.6


# OrPerceptron class
# Inherits from Perceptron class with corresponding weights and bias
class OrPerceptron(SigmoidNeuron):
    def __init__(self):
        self.w1 = 0.5
        self.w2 = 0.5
        self.bias = -0.05
        self.threshold = 0.5


# NandPerceptron class
# Inherits from Perceptron class with corresponding weights and bias
class NandPerceptron(SigmoidNeuron):
    def __init__(self):
        self.w1 = -0.5
        self.w2 = -0.5
        self.bias = 0.5
        self.threshold = 0.4