# Perceptron class
# Default weights and bias
class Perceptron:
    def __init__(self):
        self.w1 = 0
        self.w2 = 0
        self.bias = 0

    #Calculates result for inputs x1 and x2
    #x1 and x2 are bits
    def operate(self, x1, x2):
        return 1 if x1*self.w1 + x2*self.w2 + self.bias > 0 else 0

#AndPerceptron class
#Inherits from Perceptron class with corresponding weights and bias
class AndPerceptron(Perceptron):
    def __init__(self):
        self.w1 = 1
        self.w2 = 1
        self.bias = -1.5

#OrPerceptron class
#Inherits from Perceptron class with corresponding weights and bias
class OrPerceptron(Perceptron):
    def __init__(self):
        self.w1 = 1
        self.w2 = 1
        self.bias = -0.5

#NandPerceptron class
#Inherits from Perceptron class with corresponding weights and bias
class NandPerceptron(Perceptron):
    def __init__(self):
        self.w1 = -2
        self.w2 = -2
        self.bias = 3
