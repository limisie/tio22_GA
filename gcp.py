from collections import Counter

COLORS = ['orange', 'y', 'skyblue', 'rebeccapurple', 'orangered', 'gold', 'dodgerblue', 'palevioletred', 'slategray',
          'lavenderblush']


class GCP:
    def __init__(self, graph, k, ff='basic'):
        self.chromatic_number = k
        self.graph = graph
        self.ff = ff
        # self.max_cols = 5

    def get_solution_props(self):
        return len(self.graph), self.chromatic_number

    def set_graph_colors(self, solution):
        color_map = []

        for color_index in solution:
            color_map.append(COLORS[color_index])

        self.graph.color_map = color_map

    def is_valid_solution(self, solution):
        return self.non_valid_edges_count(solution) == 0

    def valid_edges_count(self, solution):
        count = 0
        for v1, v2 in zip(self.graph.adjacency_matrix.row, self.graph.adjacency_matrix.col):
            if solution[v1] != solution[v2]:
                count += 1
        return count

    def non_valid_edges_count(self, solution):
        count = 0
        for v1, v2 in zip(self.graph.adjacency_matrix.row, self.graph.adjacency_matrix.col):
            if solution[v1] == solution[v2]:
                count += 1
        return count

    def fitness_function(self, solution):
        match self.ff:
            case 'less_colors':
                return self.fitness_function_less_colors(solution)
            case 'balanced':
                return self.fitness_function_balanced(solution)
            case _:
                return self.fitness_function_basic(solution)

    def fitness_function_basic(self, solution):
        return 1 / (self.non_valid_edges_count(solution) + 1)

    def fitness_function_balanced(self, solution):
        edges_size = len(self.graph.graph.edges)
        nodes_size = len(self.graph.graph.nodes)

        occurrences = Counter(solution).values()
        color_factor = 1
        for color_occurrences in occurrences:
            color_factor *= color_occurrences / nodes_size

        return (self.valid_edges_count(solution) / edges_size) + color_factor

    def fitness_function_less_colors(self, solution):
        used_colors = len(set(solution))
        return 1 / (self.non_valid_edges_count(solution) + 1) * self.max_cols / used_colors

    def plot_graph(self):
        self.graph.show()
