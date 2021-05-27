import numpy as np
import random

class NeuralNetwork:
    def __init__(self,sizes):
        #(2,4,2)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                            for x, y in zip(sizes[:-1],sizes[1:])]
    
    def feedforward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = self.sigmoid(np.dot(w, a)+b)            
        return a
    
    def sigmoid(self, z):
        return 1.0/(1.0+np.exp(-z))