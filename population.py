import numpy as np
from member import Member

class Population:
    def __init__(self, popsize):
        self.population = []
        for i in range(popsize):
            self.population.append(Member())
    
    def think(self, a):
        self.answers = []
        for m in self.population:
            self.answers.append(m.think(a))
        return self.answers
    
    def calcfitness(self, input, desiredoutput):
        self.answers = self.think(input)
        desired = []
        for i in range(len(self.answers)):
            desired.append(desiredoutput)
        
        differences = []
        for a, d in zip(self.answers,desired):
            differences.append(abs(a-d))
        mindif = np.Infinity
        maxdif = 0
        for d in differences:
            if d < mindif:
                mindif = d                
            if d > maxdif:
                maxdif = d
        for i in range(len(differences)):
            d = differences[i]
            m = self.population[i]
            f = self.mapto(d, mindif, maxdif, 0, 1)
            print(f)
            m.updatefitness(f)

    
    def mapto(self, x, minx, maxx, miny, maxy):
        tmaxx = maxx-minx
        tmaxy = maxy-miny
        scale = tmaxy/tmaxx   
        x = x-minx
        x *= scale
        x += miny
        return x



