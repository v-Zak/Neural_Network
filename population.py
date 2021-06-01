from typing import ByteString
import numpy as np
import math
import random

from numpy.lib.function_base import average
from member import Member

class Population:
    def __init__(self, popsize):
        self.population = []
        self.generation = 1
        for i in range(popsize):
            self.population.append(Member())
    
    def think(self, a):
        self.answers = []
        for m in self.population:
            self.answers.append(m.think(a))
        return self.answers
    
    def calcFitness(self, input, desiredoutput):
        self.answers = self.think(input)
        desired = []
        for i in range(len(self.answers)):
            desired.append(desiredoutput)
        
        self.differences = []
        for a, d in zip(self.answers,desired):
            self.differences.append(abs(a-d))
        mindif = np.Infinity
        maxdif = 0
        for i in range(len(self.differences)):
            d = self.differences[i]
            if d < mindif:
                mindif = d            
            if d > maxdif:
                maxdif = d
        for i in range(len(self.differences)):        
            d = self.differences[i]
            m = self.population[i]
            f = self.mapto(d, mindif, maxdif, 1, 0)
            m.updatefitness(f)
        
        print(f"The best answer is: {self.bestAns()}")
        print(f"The average answer is: {self.averageAns()}")   

    def asexualReproduction(self):
        newPopulation = []
        matingPool = []        
        scale = 10 #how much to scale the fitness function by
        for i in range(len(self.population)):
            m = self.population[i]
            f = m.fitness                  
            for j in range(math.floor(f*scale+1)):
                matingPool.append(self.population[i])
        
        for i in range(len(self.population)):
            index = random.randint(0,len(matingPool)-1)
            index = math.floor(index)
            m = matingPool[index]
            newPopulation.append(m)
        self.population = newPopulation.copy()
        self.generation += 1

    def evolve(self,iter,input, desiredOutput): 
        for i in range(iter):
            print(f"Generation {self.generation}")
            self.calcFitness(input, desiredOutput)
            self.asexualReproduction()
            self.mutatePopulation(0.05)
            print("\n")

    def mutatePopulation(self, mutationChance):
        for m in self.population:
            m.mutate(mutationChance)

    def bestAns(self):
        dif = np.Infinity
        for i in range(len(self.differences)):
            d = self.differences[i]
            if d < dif:
              dif = d
              best = self.answers[i] 
        return best

    def averageAns(self):
        total = 0
        quantity = len(self.answers)
        for a in self.answers:
            total += a
        return total/quantity   
    
    def mapto(self, x, minx, maxx, miny, maxy):
        difx = maxx-minx
        dify = maxy-miny
        if not (difx == 0):
            scale = dify/difx   
        x = x-minx
        if not (difx == 0):
            x *= scale
        x += miny
        return x



