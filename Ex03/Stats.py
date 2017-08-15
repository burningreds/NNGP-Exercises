#import matplotlib.pyplot as plt
from SigmoidNeuron import *


def main():
    m = random.uniform(-5, 5)
    n = random.randint(-25, 25)
    print "Random slope (m): " + str(m)
    print "Random y-intercept (n): " + str(n)
    neuron = LearningNeuron()
    x = range(1, 300)
    successRates = [0]*len(x)

    for i in range(1, len(x)):
        neuron.training(m, n, x[i])
        successRates[i] = neuron.classifyPoints(m, n, 100)

    plt.plot(x, successRates)
    plt.axis([0, 300, 0, 1])
    plt.show()

if __name__ == "__main__":
    main()