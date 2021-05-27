from neuralnetwork import NeuralNetwork

class Member:
    def __init__(self):
        self.brain = NeuralNetwork([1,2,1])
        self.fitness = 0       

    def think(self, a):
        return self.brain.feedforward(a)
    
    def updatefitness(self,f):
        self.fitness = f