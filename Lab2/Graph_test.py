import unittest
from Graph import *


class TestGraph(unittest.TestCase):
    def test_init_undirected_graph(self):
        graph_undirected = UndirectedGraph(5)

        self.assertEqual(graph_undirected.graph, [[0]*5]*5)

    def test_add_vertex_undirected_graph(self):
        graph_undirected = UndirectedGraph(5)

        graph_undirected.add_vertex(5)

        self.assertEqual(graph_undirected.graph, [[0]*6]*6)

    def test_add_edge_undirected_graph(self):
        excepted = [[0 for _ in range(5)] for _ in range(5)]
        excepted[0][1] = 1
        excepted[1][0] = 1
        graph_undirected = UndirectedGraph(5)

        graph_undirected.add_edge(0, 1)

        self.assertEqual(graph_undirected.graph, excepted)

    def test_remove_vertex_undirected_graph(self):
        graph_undirected = UndirectedGraph(5)

        graph_undirected.add_edge(0, 1)
        graph_undirected.remove_vertex(0)

        self.assertEqual(graph_undirected.graph, [[0]*4]*4)

    def test_remove_edge_undirected_graph(self):
        graph_undirected = UndirectedGraph(5)

        graph_undirected.add_edge(0, 1)
        graph_undirected.remove_edge(0, 1)

        self.assertEqual(graph_undirected.graph, [[0]*5]*5)

    def test_init_directed_graph(self):
        graph_directed = DirectedGraph(5)

        self.assertEqual(graph_directed.graph, [[0]*5]*5)

    def test_add_vertex_directed_graph(self):
        graph_directed = DirectedGraph(5)

        graph_directed.add_vertex(5)

        self.assertEqual(graph_directed.graph, [[0]*6]*6)

    def test_add_edge_directed_graph(self):
        excepted = [[0 for _ in range(5)] for _ in range(5)]
        excepted[0][1] = 1
        graph_directed = DirectedGraph(5)

        graph_directed.add_edge(0, 1)

        self.assertEqual(graph_directed.graph, excepted)

    def test_remove_vertex_directed_graph(self):
        graph_directed = DirectedGraph(3)

        graph_directed.add_edge(0, 1)
        graph_directed.add_edge(1, 0)
        graph_directed.remove_vertex(0)

        self.assertEqual(graph_directed.graph, [[0]*2]*2)

    def test_remove_edge_directed_graph(self):
        graph_directed = DirectedGraph(5)

        graph_directed.add_edge(0, 1)
        graph_directed.remove_edge(0, 1)

        self.assertEqual(graph_directed.graph, [[0]*5]*5)

    def test_init_weighted_graph_undirected(self):
        graph_weighted_undirected = WeightedGraphUndirected(5)

        self.assertEqual(graph_weighted_undirected.graph, [[0]*5]*5)

    def test_add_vertex_weighted_graph_undirected(self):
        graph_weighted_undirected = WeightedGraphUndirected(5)

        graph_weighted_undirected.add_vertex(5)

        self.assertEqual(graph_weighted_undirected.graph, [[0]*6]*6)

    def test_add_edge_weighted_graph_undirected(self):
        graph_weighted_undirected = WeightedGraphUndirected(5)

        graph_weighted_undirected.add_edge(0, 1, 13)

        self.assertEqual(graph_weighted_undirected.graph, [[0, 13, 0, 0, 0], [13, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

    def test_remove_vertex_weighted_graph_undirected(self):
        graph_weighted_undirected = WeightedGraphUndirected(5)

        graph_weighted_undirected.add_edge(0, 1, 13)
        graph_weighted_undirected.remove_vertex(0)

        self.assertEqual(graph_weighted_undirected.graph, [[0]*4]*4)

    def test_remove_edge_weighted_graph_undirected(self):
        graph_weighted_undirected = WeightedGraphUndirected(5)

        graph_weighted_undirected.add_edge(0, 1, 13)
        graph_weighted_undirected.remove_edge(0, 1)

        self.assertEqual(graph_weighted_undirected.graph, [[0]*5]*5)

    def test_init_weighted_graph_directed(self):
        graph_weighted_directed = WeightedGraphDirected(5)

        self.assertEqual(graph_weighted_directed.graph, [[0]*5]*5)

    def test_add_vertex_weighted_graph_directed(self):
        graph_weighted_directed = WeightedGraphDirected(5)

        graph_weighted_directed.add_vertex(5)

        self.assertEqual(graph_weighted_directed.graph, [[0]*6]*6)

    def test_add_edge_weighted_graph_directed(self):
        graph_weighted_directed = WeightedGraphDirected(5)

        graph_weighted_directed.add_edge(0, 1, 13)

        self.assertEqual(graph_weighted_directed.graph, [[0, 13, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

    def test_remove_vertex_weighted_graph_directed(self):
        graph_weighted_directed = WeightedGraphDirected(5)

        graph_weighted_directed.add_edge(0, 1, 13)
        graph_weighted_directed.remove_vertex(0)

        self.assertEqual(graph_weighted_directed.graph, [[0]*4]*4)

    def test_remove_edge_weighted_graph_directed(self):
        graph_weighted_directed = WeightedGraphDirected(5)

        graph_weighted_directed.add_edge(0, 1, 13)
        graph_weighted_directed.remove_edge(0, 1)

        self.assertEqual(graph_weighted_directed.graph, [[0]*5]*5)


if __name__ == '__main__':
    unittest.main()
