from crossover import SinglePointCrossover
from dimacs_reader import dimacs_to_adjacent_matrix
from gcp import GCP
from graph import Graph
from mutation import RandomResetting
from optimizer import GeneticAlgorithm
from selection import RandomSelection, StochasticSelection, RouletteWheelSelection
from stop_conditions import StopWhenFit, StopAfterNIterations


def random_instance(n):
    return GCP(Graph(n=n), k=n, ff='basic')


def myciel(n):
    nodes, am, k = dimacs_to_adjacent_matrix(f'./instances/myciel{n}.txt')
    return GCP(Graph(adjacent_matrix=am), k=k, ff='basic')


def optimize(gcp):
    ga = GeneticAlgorithm(gcp, 50)

    ga.add_stop_condition(StopAfterNIterations(n=100))
    # ga.add_stop_condition(StopWhenFit(expected_fitness=1))
    ga.selection_op = RouletteWheelSelection()
    ga.crossover_op = SinglePointCrossover(p=.3)
    ga.mutation_op = RandomResetting(p=.1)

    solution = ga.optimize()
    print(solution)
    print(gcp.is_valid_solution(solution))
    print(len(set(solution)))
    gcp.set_graph_colors(solution)
    gcp.plot_graph()


def main():
    # optimize(random_instance())
    optimize(myciel(4))


if __name__ == '__main__':
    main()
