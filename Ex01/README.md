https://github.com/burningreds/NNGP-Exercise-1

# Exercise 01
For "Neural Networks and Genetic Programming" course

1. Implement a Perceptron with the AND, OR, NAND behavior
2. Implement the summing number gate

### How to run
- Every perceptron receives bits. You can simply run Perceptron.py and create the perceptron you wish, then use it to operate two bits with the method 'operate'. For example: 

```python
andPerceptron = AndPerceptron()
andPerceptron.operate(1, 1)
#output should be 1
```

- A similar procedure can be used for SummingNumberGate.py which contains the implementation for the summing number gate.
- The output is a pair (carry, sum)

```python
summingGate = SummingNumberGate()
summingGate.operate(1, 1)
#output should be (1, 0)
```

- And you can run the tests created for each class (Tests.py).
