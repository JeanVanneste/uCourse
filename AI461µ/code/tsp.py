# tsp.py
# Author: Sébastien Combéfis
# Version: April 26, 2020

import array
import numpy
import random

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

INF = float('inf')
DIST = [
    [INF, 1  , INF, INF, INF, INF, INF, 1  ],
    [1  , INF, 1  , INF, INF, INF, INF, INF],
    [INF, 1  , INF, 1  , INF, INF, INF, INF],
    [INF, INF, 1  , INF, 1  , INF, INF, INF],
    [INF, INF, INF, 1  , INF, 1  , INF, INF],
    [INF, INF, INF, INF, 1  , INF, 1  , INF],
    [INF, INF, INF, INF, INF, 1  , INF, 1  ],
    [1  , INF, INF, INF, INF, INF, 1  , INF]
]
#DIST = [
#    [INF, 20 , 42 , 35 ],
#    [20 , INF, 30 , 34 ],
#    [42 , 30 , INF, 12 ],
#    [35 , 34 , 12 , INF]
#]
def distance(ind):
    dist = 0
    for i in range(IND_SIZE):
        dist += DIST[ind[i]][ind[(i+1) % IND_SIZE]]
    return dist

# Defining the individuals.
creator.create('FitnessMax', base.Fitness, weights=(1.0,))
creator.create('Individual', array.array, typecode='i', fitness=creator.FitnessMax)

# Initialising the population.
IND_SIZE = len(DIST)
toolbox = base.Toolbox()
toolbox.register('indices', random.sample, range(IND_SIZE), IND_SIZE)
toolbox.register('individual', tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register('population', tools.initRepeat, list, toolbox.individual)

# Defining the fitness function.
def evaluate(ind):
    return 1.0 / distance(ind),
toolbox.register('evaluate', evaluate)

# Defining the mating function.
toolbox.register('mate', tools.cxOrdered)

# Defining the mutation function.
def mutate(ind):
    src = random.randint(0, IND_SIZE-1)
    dst = src
    while dst == src:
        dst = random.randint(0, IND_SIZE-1)
    ind[src], ind[dst] = ind[dst], ind[src]
    return ind,
toolbox.register('mutate', mutate)

# Defining the selection function.
toolbox.register('select', tools.selBest)


# Running the simulation.
if __name__ == '__main__':
    population = toolbox.population(n=10)

    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register('avg', numpy.mean)
    stats.register('std', numpy.std)
    stats.register('min', numpy.min)
    stats.register('max', numpy.max)

    population, log = algorithms.eaSimple(population, toolbox, 0.5, 0.2, 10000, stats, hof, False)

    print('Final population:\n', '\n '.join('{}: {}'.format(ind.tolist(), ind.fitness.values[0]) for ind in population), '\n')
    print('Hall of Fame:\n', '{}: {}'.format(hof[0].tolist(), hof[0].fitness.values[0]))
    with open('tsp-ga-log.txt', 'w') as file:
        file.write(str(log))
