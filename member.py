from neuralnetwork import NeuralNetwork

class Member:
    def __init__(self):
        self.brain = NeuralNetwork([1,2,1])
        self.fitness = 0       

    def think(self, a):
        return float(self.brain.feedforward(a)[0][0])

    def mutate(self, mutationRate):
        self.brain.mutate(mutationRate)
    
    def updatefitness(self,f):
        self.fitness = f
