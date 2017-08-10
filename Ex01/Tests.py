import unittest
from Perceptron import *
from SummingNumberGate import *


# Tests for all classes
# Run to excecute all tests

# AndPerceptron tests
class AndCase(unittest.TestCase):
    def setUp(self):
        self.andPerceptron = AndPerceptron()

    def testA(self):
        assert self.andPerceptron.operate(1, 1) == 1, "operate() in AndPerceptron not calculating values correctly"

    def testB(self):
        assert self.andPerceptron.operate(1, 0) == 0, "operate() in AndPerceptron not calculating values correctly"

    def testC(self):
        assert self.andPerceptron.operate(0, 1) == 0, "operate() in AndPerceptron not calculating values correctly"

    def testD(self):
        assert self.andPerceptron.operate(0, 0) == 0, "operate() in AndPerceptron not calculating values correctly"


# OrPerceptron tests
class OrCase(unittest.TestCase):
    def setUp(self):
        self.orPerceptron = OrPerceptron()

    def testA(self):
        assert self.orPerceptron.operate(1, 1) == 1, "operate() in OrPerceptron not calculating values correctly"

    def testB(self):
        assert self.orPerceptron.operate(1, 0) == 1, "operate() in OrPerceptron not calculating values correctly"

    def testC(self):
        assert self.orPerceptron.operate(0, 1) == 1, "operate() in OrPerceptron not calculating values correctly"

    def testD(self):
        assert self.orPerceptron.operate(0, 0) == 0, "operate() in OrPerceptron not calculating values correctly"


# NandPerceptron tests
class NandCase(unittest.TestCase):
    def setUp(self):
        self.nandPerceptron = NandPerceptron()

    def testA(self):
        assert self.nandPerceptron.operate(10, 1) == 0, "operate() in NandPerceptron not calculating values correctly"

    def testB(self):
        assert self.nandPerceptron.operate(1, 0) == 1, "operate() in NandPerceptron not calculating values correctly"

    def testC(self):
        assert self.nandPerceptron.operate(0, 1) == 1, "operate() in NandPerceptron not calculating values correctly"

    def testD(self):
        assert self.nandPerceptron.operate(0, 0) == 1, "operate() in NandPerceptron not calculating values correctly"


# SumingNumberGate tests
class SummingNumberCase(unittest.TestCase):
    def setUp(self):
        self.sum = SummingNumberGate()

    def testA(self):
        assert self.sum.operate(1, 1) == (1, 0), "operate() in SummingNumberGate not calculating values correctly"

    def testB(self):
        assert self.sum.operate(0, 1) == (0, 1), "operate() in SummingNumberGate not calculating values correctly"

    def testC(self):
        assert self.sum.operate(1, 0) == (0, 1), "operate() in SummingNumberGate not calculating values correctly"

    def testD(self):
        assert self.sum.operate(0, 0) == (0, 0), "operate() in SummingNumberGate not calculating values correctly"


if __name__ == '__main__':
    unittest.main(exit=False)
