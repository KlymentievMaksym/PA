import numpy as np


class Graph:
    def __init__(self, number_of_vertices: int):
        self.number_of_vertices = number_of_vertices
        self.graph = [[0 for _ in range(number_of_vertices)] for _ in range(number_of_vertices)]

    def convertator(self, type_of_realization: str, *args, **kwargs):
        if not isinstance(type_of_realization, str) and type_of_realization != 'list':
            raise NameError(f"Not expected type of realization, expected 'list', got {type_of_realization}")

        if len(args) >= 1:
            raise OverflowError(f"Not expected number of arguments, expected 1, got {len(args)}")

        if type_of_realization == 'list':
            matrix = self.graph
            dict_of_lists_to_return = {}
            for vertex in range(self.number_of_vertices):
                dict_of_lists_to_return[vertex] = []
                for vertex_second in range(self.number_of_vertices):
                    if matrix[vertex][vertex_second] != 0:
                        dict_of_lists_to_return[vertex].append(vertex_second)
            return dict_of_lists_to_return

    def add_edge(self, v1: int, v2: int, weight: int):
        self.graph[v1][v2] = weight
        self.graph[v2][v1] = weight

    def remove_edge(self, v1: int, v2: int):
        self.graph[v1][v2] = 0
        self.graph[v2][v1] = 0

    def random_graph_Erdos_Renyi(self, probability: float):
        weight = 1
        if probability < 0 or probability > 1:
            raise ValueError("Probability can't be less than 0 or more than 1")

        for i in range(self.number_of_vertices):
            for j in range(i+1, self.number_of_vertices):
                success = np.random.choice([True, False], p=[probability, 1 - probability])
                if success:
                    self.add_edge(i, j, weight)
                else:
                    self.remove_edge(i, j)

        return self.graph
