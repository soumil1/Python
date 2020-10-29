"""
A simple (machine learning?) program that takes in an array and its outputs to train and then predict an output for some test case.

Note: This program is very simple program and computes the very basic linear math. It cannot and will not give accurate results.
This is just to give a glimpse of how ML works.
"""

import numpy as np

class Network:
	def __init__(self):
		np.random.seed(1)
		self.weights = 2 * np.random.random((2, 1)) - 1
	
	def train(self, inputs, outputs, num):
		for i in range(num):
			output = self.think(inputs)
			loss = outputs - output
			adjustment = 0.01 * np.dot(inputs.T, loss)
			self.weights += adjustment

	def think(self, inputs):
		return np.dot(inputs, self.weights)

# Here the network attempts to identify 2*(a+b) without having to explicitly define that to the program.
# inputs is a 2D array in format - [[a, b], [a, b], [a, b]... till n] each list [a, b] is a training set.
# outputs is also a 2D array in format - [[r, r, r, r, ... till n]] where r is the result of each trainging set.
network = Network()
inputs = np.array([[2, 3], [1, 1], [5, 2], [12, 3]]) # Array containing two variable list [a, b]
outputs = np.array([[10, 4, 14, 30]]).T # Output array for each list in inputs
network.train(inputs, outputs, 1000) # Take the inputs and predict output for each input and try to rectify the prediction error
print(np.around(network.think(np.array([5, 7])))) # Test case

# Here the inputs and outputs are in the same format.
# Here the network attempts to identify absolute value of a-b
network = Network()
inputs = np.array([[2, 3], [1, 1], [5, 2], [12, 3]])
outputs = np.array([[1, 0, 3, 9]]).T
network.train(inputs, outputs, 10000)
print(np.around(network.think(np.array([8, 2]))))