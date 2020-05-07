# maxone.py
# Author: Sébastien Combéfis
# Version: April 26, 2020

import random

IND_SIZE = 10
POP_SIZE = 6

# Initialising the population.
population = []
for k in range(POP_SIZE):
    ind = []
    for i in range(IND_SIZE):
        if random.random() < 0.5:
            ind.append(1)
        else:
            ind.append(0)
    population.append(ind)

# Defining the fitness function.
def evaluate(ind):
    return sum(ind)/len(ind)

# Defining the mating function.
def mate(ind1, ind2):
    return ind1, ind2

# Defining the mutation function.
def mutate(ind):
    return ind

# Defining the selection function.
def select(pop):
    max = sum(evaluate(ind) for ind in pop)
    prob_list = [0]
    for ind in pop:
        prob_list.append((evaluate(ind) / max) + prob_list[-1])
    var = random.random()
    for 


# Running the simulation.
if __name__ == '__main__':
    PROB_MATING = 0.5
    PROB_MUTATION = 0.2
    ITERATIONS = 100

    for i in population:
        print(evaluate(i))

    print(select(population))
