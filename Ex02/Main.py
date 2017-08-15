from Perceptron import *


def main():
    m = random.uniform(-5, 5)
    n = random.randint(-25, 25)
    print "Random slope (m): " + str(m)
    print "Random y-intercept (n): " + str(n)
    perceptron = LearningPerceptron()
    print "Training..."
    perceptron.training(m, n, 10000)
    print "Testing..."
    perceptron.test(m, n, 300)


if __name__ == "__main__":
    main()