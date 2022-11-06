import math
from abc import ABC

import numpy as np

from population import Population


class Optimizer(ABC):
    def __init__(self, problem):
        self.problem = problem

        self.iteration = 0
        self.stop_conditions = []

        self.best_solution_history = []
        self.best_fitness_history = []
        self.best_solution = None
        self.best_fitness = 0

    def fitness_function(self, solution):
        return self.problem.fitness_function(solution)

    def add_stop_condition(self, sc):
        self.stop_conditions.append(sc)
        sc.optimizer = self

    def is_stop_condition_satisfied(self):
        for sc in self.stop_conditions:
            if sc.is_stop():
                return True
        return False


class GeneticAlgorithm(Optimizer):
    def __init__(self, problem, population_size=100):
        super().__init__(problem)
        self.population_size = population_size
        self.chromosome_size, self.max_gene_value = self.problem.get_solution_props()
        self.population = None

        self.avg_fitness_history = []
        self.selection_op = None
        self.crossover_op = None
        self.mutation_op = None

    def optimize(self):
        self.population = Population(self.chromosome_size, self.population_size, self.max_gene_value)
        self.population.fitness = self.get_population_fitness()

        while not self.is_stop_condition_satisfied():
            parents = self.selection_op.get_parents(self.population)
            children = self.crossover_op.get_children(parents)
            children = self.mutation_op.mutate_population(children, self.max_gene_value)

            self.population.individuals = children
            self.population.fitness = self.get_population_fitness()

            self.log()
            self.iteration += 1

        self.log()
        return self.best_solution

    def set_selection_method(self, selection):
        self.selection_op = selection

    def get_population_fitness(self):
        fitness = []

        for individual in self.population:
            fitness.append(self.problem.fitness_function(individual))

        return fitness

    def log(self):
        avg_fitness = np.average(self.population.fitness)
        self.avg_fitness_history.append(avg_fitness)

        best_in_generation = self.population[np.argmax(self.population.fitness)]
        best_in_generation_fitness = max(self.population.fitness)
        self.best_solution_history.append(best_in_generation)
        self.best_fitness_history.append(best_in_generation_fitness)

        if best_in_generation_fitness > self.best_fitness:
            self.best_fitness = best_in_generation_fitness
            self.best_solution = best_in_generation
