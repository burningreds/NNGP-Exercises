from Perceptron import *


# Uses nands to sum bits
class SummingNumberGate:
    def __init__(self):
        self.nand = NandPerceptron()

    # Inputs x1 and x2 are bits
    # Output is a pair (carry, sum)
    def operate(self, x1, x2):
        x3 = self.nand.operate(x1, x2)
        x4 = self.nand.operate(x1, x3)
        x5 = self.nand.operate(x3, x2)
        resCarry = self.nand.operate(x3, x3)
        resSum = self.nand.operate(x4, x5)
        return resCarry, resSum
