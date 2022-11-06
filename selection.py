import random
from abc import ABC, abstractmethod
from operator import itemgetter

import numpy as np


class Selection(ABC):

    @abstractmethod
    def _index_generator(self, population):
        pass

    def get_parents(self, population):
        parents = []

        for i in self._index_generator(population):
            parents.append(population[i])

        return np.array(parents)


class RandomSelection(Selection):
    def __init__(self, seed=42):
        super().__init__()
        np.random.seed(seed)

    def _index_generator(self, population):
        for _ in population:
            yield np.random.randint(len(population))


class RouletteWheelSelection(Selection):

    def _index_generator(self, population):
        fitness_sum = sum(population.fitness)
        proportions = population.fitness / fitness_sum

        for _ in population:
            yield np.random.choice(range(len(population)), p=proportions)


class TournamentSelection(Selection):
    def __init__(self, k):
        super().__init__()
        self.k = k

    def _index_generator(self, population):
        for _ in population:
            k_indices = random.sample(range(len(population)), self.k)
            k_group = [(i, population.fitness[i]) for i in k_indices]
            yield max(k_group, key=itemgetter(1))[0]


class StochasticSelection(Selection):

    def _index_generator(self, population):
        fitness_scale = []
        pointers = []
        pointer_step = sum(population.fitness) / len(population)
        offset = np.random.uniform(0, pointer_step)

        for i, fitness in enumerate(population.fitness):
            if i == 0:
                fitness_scale.append(fitness)
                pointers.append(offset)
            else:
                fitness_scale.append(fitness + fitness_scale[i - 1])
                pointers.append(pointers[i - 1] + pointer_step)

        i = 0
        for p in pointers:
            while fitness_scale[i] < p:
                i += 1
            yield i


def set_population_fitness(population):
    fitness = []
    for chromosome in population:
        fitness.append(sum(chromosome))
    print(fitness)
    return fitness
