import random
import matplotlib.pyplot as plt
import numpy as np


# Perceptron class
# Default weights and bias
class Perceptron:
    def __init__(self):
        self.w1 = 0
        self.w2 = 0
        self.bias = 0

    def setW1(self, newWeight):
        self.w1 = newWeight

    def setW2(self, newWeight):
        self.w2 = newWeight

    # Calculates result for inputs x1 and x2
    # x1 and x2 are bits
    def operate(self, x, y):
        return 1 if x * self.w1 + y * self.w2 + self.bias > 0 else 0


# Perceptron that learns how to identify
# if a x y point is above or below a line
class SigmoidNeuron(Perceptron):
    def __init__(self):
        self.threshold = 0.5

    def operate(self, x, y):
        return 1 if self.sigmoidFunction(x, y) > self.threshold else 0

    def sigmoidFunction(self, x, y):
        return 1 / np.exp(x * self.w1 + y * self.w2 + self.bias)

class LearningNeuron(SigmoidNeuron):
    def __init__(self):
        self.w1 = 1
        self.w2 = 1
        self.bias = 0.5
        self.c = 0.01
        self.threshold = 0.1

    # Modifies weights accordingly if
    # calculated output is different from desired output
    def train(self, x, y, desOut):
        out = self.operate(x, y)
        if desOut == 0 and out == 1:
            self.setW1(self.w1 - self.c * x)
            self.setW2(self.w2 - self.c * y)
        elif desOut == 1 and out == 0:
            self.setW1(self.w1 + self.c * x)
            self.setW2(self.w2 + self.c * y)

    # Training for the perceptron to identify a line
    # determined by slope m and y-intercept n
    def training(self, m, n):
        for a in range(0, 10000):
            x = random.randint(-50, 50)
            y = random.randint(-50, 50)
            out = 1 if m * x + n - y > 0 else 0
            self.train(x, y, out)

    # "Tests" the training by plotting random points (300)
    # classified by perceptron for line determined by m and n
    # Calculates success rate
    def test(self, m, n):
        # y = mx + n
        xVector = range(-100, 100)
        yVector = [(i * m + n) for i in xVector]
        plt.plot(xVector, yVector)
        successCount = 0
        for a in range(0, 300):
            x = random.randint(-50, 50)
            y = random.randint(-50, 50)
            out = self.operate(x, y)
            desOut = 1 if m * x + n - y > 0 else 0
            if out == desOut:
                successCount += 1
            colour = 'ro' if out == 1 else 'bo'
            plt.plot(x, y, colour)
        print "Success rate: " + str(successCount / 300.0)
        plt.axis([-100, 100, -100, 100])
        plt.show()