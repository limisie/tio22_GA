from abc import ABC, abstractmethod
import numpy as np


def pair_generator(population_size):
    indices = [i for i in range(population_size)]
    np.random.shuffle(indices)
    for _ in range(population_size // 2):
        yield [indices.pop(), indices.pop()]


class Crossover(ABC):
    def __init__(self, p=0.4):
        self.p = p

    @abstractmethod
    def cross(self, parent1, parent2):
        pass

    def get_children(self, parents):
        population_size = len(parents)
        children = []

        for parent1, parent2 in pair_generator(population_size):
            if np.random.rand() <= self.p:
                child1, child2 = self.cross(parents[parent1], parents[parent2])
                children.append(child1)
                children.append(child2)
            else:
                children.append(parents[parent1])
                children.append(parents[parent2])

        return np.array(children)


class SinglePointCrossover(Crossover):
    def __init__(self, p=0.4):
        super().__init__(p)

    def cross(self, parent1, parent2):
        chromosome_size = len(parent1)
        locus = np.random.randint(chromosome_size)

        child1 = np.concatenate((parent1[:locus], parent2[locus:]))
        child2 = np.concatenate((parent2[:locus], parent1[locus:]))

        return child1, child2


class MultiPointCrossover(Crossover):
    def __init__(self, locus_count, p=0.4):
        super().__init__(p)
        self.locus_count = locus_count

    def cross(self, parent1, parent2):
        chromosome_size = len(parent1)
        loci = [np.random.randint(chromosome_size) for _ in range(self.locus_count)]
        loci.sort()
        prev_locus = 0

        child1_genes = []
        child2_genes = []

        for locus in loci:
            child1_genes.append(parent1[prev_locus:locus])
            child2_genes.append(parent2[prev_locus:locus])

            parent1, parent2 = parent2, parent1
            prev_locus = locus

        child1_genes.append(parent1[prev_locus:])
        child2_genes.append(parent2[prev_locus:])

        return np.concatenate(child1_genes), np.concatenate(child2_genes)


class UniformCrossover(Crossover):
    def __init__(self, p=0.4):
        super().__init__(p)

    def cross(self, parent1, parent2):
        chromosome_size = len(parent1)

        child1_genes = []
        child2_genes = []
        parents = [parent1, parent2]

        for i in range(chromosome_size):
            gene_activator = np.random.randint(2)
            child1_genes.append(parents[gene_activator][i])
            child2_genes.append(parents[abs(gene_activator - 1)][i])

        return np.array(child1_genes), np.array(child2_genes)
