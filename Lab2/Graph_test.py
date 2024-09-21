import unittest
from Graph import Graph


class TestGraph(unittest.TestCase):
    def test_init(self):
        test_graph = Graph(5)
        self.assertEqual(test_graph.number_of_vertices, 5)

    def test_add_vertex(self):
        test_graph = Graph(5)
        test_graph.add_vertex(5)
        self.assertEqual(test_graph.graph[5][5], 0)

    def test_add_edge(self):
        test_graph = Graph(5)
        test_graph.add_edge(0, 1)
        self.assertEqual(test_graph.graph[0][1], 1)
        self.assertEqual(test_graph.graph[1][0], 1)

    def test_delete_vertex(self):
        test_graph = Graph(5)
        test_graph.add_vertex(5)
        test_graph.delete_vertex(5)
        self.assertEqual(test_graph.graph[5][5], 0)

    def test_remove_edge(self):
        test_graph = Graph(5)
        test_graph.add_edge(0, 1)
        test_graph.remove_edge(0, 1)
        self.assertEqual(test_graph.graph[0][1], 0)
        self.assertEqual(test_graph.graph[1][0], 0)


if __name__ == '__main__':
    unittest.main()
