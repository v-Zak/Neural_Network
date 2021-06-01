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

    def mutate(self, mutationRate):
        #mutationRate = chance of a mutation occuring in whole brain
        if random.random() <= mutationRate:
            i = 0                       
            for layer in self.biases:
                j = 0
                for bias in layer:
                    change = (random.random()-0.5)/10
                    bias += change
                    self.biases[i][j] = bias
                    j += 1
                i += 1
            i = 0
            for layer in self.weights:
                j = 0
                for weights in layer:
                    z = 0
                    for weight in weights:
                        change = (random.random()-0.5)/10
                        weight += change
                        self.weights[i][j][z] = weight
                        z += 1
                    j += 1
                i += 1
    
    def sigmoid(self, z):
        return 1.0/(1.0+np.exp(-z))
    
