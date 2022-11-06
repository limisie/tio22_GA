from crossover import SinglePointCrossover
from gcp import GCP
from graph import Graph
from mutation import RandomResetting
from optimizer import GeneticAlgorithm
from selection import RandomSelection
from stop_conditions import StopWhenFit, StopAfterNIterations


def main():
    n = 10

    gcp = GCP(Graph(n=n), k=n, ff='less_colors')
    ga = GeneticAlgorithm(gcp, 1000)

    # ga.add_stop_condition(StopWhenFit(expected_fitness=1.01))
    ga.add_stop_condition(StopAfterNIterations(n=100))
    ga.selection_op = RandomSelection()
    ga.crossover_op = SinglePointCrossover()
    ga.mutation_op = RandomResetting()

    solution = ga.optimize()
    print(solution)
    gcp.set_graph_colors(solution)
    gcp.plot_graph()


if __name__ == '__main__':
    main()
