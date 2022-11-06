import random
from abc import ABC, abstractmethod
import numpy as np


class Mutation(ABC):
    def __init__(self, p=0.2):
        self.p = p
        self.loci = None
        self.domain_max = None

    @abstractmethod
    def mutate_individual(self, individual):
        pass

    def set_loci(self, chromosome_size):
        loci = random.sample(range(chromosome_size), 2)
        loci.sort()
        self.loci = loci

    def mutate_population(self, population, max_value=1):
        mutated = []
        self.domain_max = max_value

        for chromosome in population:
            if np.random.rand() <= self.p:
                self.set_loci(len(chromosome))
                mutated.append(self.mutate_individual(np.array(chromosome)))
            else:
                mutated.append(chromosome)

        return np.array(mutated)


class RandomResetting(Mutation):

    def mutate_individual(self, chromosome):
        chromosome[self.loci[0]] = np.random.randint(self.domain_max)
        return chromosome


class SwapMutation(Mutation):

    def mutate_individual(self, chromosome):
        chromosome[self.loci[0]], chromosome[self.loci[1]] = \
            chromosome[self.loci[1]], chromosome[self.loci[0]]
        return chromosome


class ScrambleMutation(Mutation):

    def mutate_individual(self, chromosome):
        np.random.shuffle(chromosome[self.loci[0]:self.loci[1]])
        return chromosome


class InversionMutation(Mutation):

    def mutate_individual(self, chromosome):
        chromosome[self.loci[0]:self.loci[1]] = chromosome[self.loci[0]:self.loci[1]][::-1]
        return chromosome
