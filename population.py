import numpy as np


class Population:
    def __init__(self, gene_num, population_size, k=2):
        self.individuals = np.random.randint(0, k, (population_size, gene_num), dtype=np.int8)
        self.fitness = np.empty(population_size)
        self.k = k

    def __str__(self):
        return self.individuals.__str__()

    def __len__(self):
        return self.individuals.shape[0]

    def __getitem__(self, item):
        return self.individuals[item]

    def __iter__(self):
        return PopulationIterator(self)


class PopulationIterator:
    def __init__(self, population):
        self._population = population
        self._index = 0

    def __next__(self):
        if self._index < len(self._population):
            result = self._population[self._index]
            self._index += 1
            return result
        raise StopIteration
