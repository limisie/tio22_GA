import matplotlib.pyplot as plt
import networkx as nx
import scipy


class Graph:
    def __init__(self, n=7, p=0.5, adjacent_matrix=None):

        if adjacent_matrix is None:
            self.graph = nx.fast_gnp_random_graph(n, p)
        else:
            self.graph = nx.from_numpy_matrix(adjacent_matrix)

        self.adjacency_matrix = scipy.sparse.triu(nx.to_scipy_sparse_array(self.graph))
        self.color_map = []

    def show(self):
        plt.axis('equal')
        if self.color_map:
            nx.draw(self.graph, node_color=self.color_map, with_labels=True)
        else:
            nx.draw(self.graph, with_labels=True)
        plt.show()

    def __len__(self):
        return len(self.graph.nodes)
