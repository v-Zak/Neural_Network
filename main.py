from population import Population

population = Population(1000)
for i in range(20):
    population.evolve(1,0,1)
    population.evolve(1,1,0)
population.calcFitness(0,1)
population.calcFitness(1,0)