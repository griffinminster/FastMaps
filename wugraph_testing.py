import wugraph as graph
import unittest


class TestStringMethods(unittest.TestCase):
    @staticmethod
    def GRAPH0():
        g = graph.WuGraph(6)
        a = g.set_edge
        a(0, 1, 5)
        a(0, 2, 7)
        a(0, 3, 2)
        a(1, 4, 9)
        a(1, 5, 6)
        a(3, 5, 0)
        a(3, 4, 1)
        return g

    @staticmethod
    def GRAPH0_MST():
        g = graph.WuGraph(6)
        a = g.set_edge
        a(0, 1, 5)
        a(0, 2, 7)
        a(0, 3, 2)
        a(3, 5, 0)
        a(3, 4, 1)
        return g

    @staticmethod
    def GRAPH1():
        g = graph.WuGraph(6)
        a = g.set_edge
        a(0, 1, 12)
        a(1, 2, 31)
        a(2, 4, -2)
        a(1, 3, 56)
        a(3, 5, 1)
        a(2, 5, 7)
        a(3, 4, 9)
        return g

    @staticmethod
    def GRAPH1_MST():
        g = graph.WuGraph(6)
        a = g.set_edge
        a(0, 1, 12)
        a(1, 2, 31)
        a(2, 4, -2)
        a(2, 5, 7)
        a(3, 5, 1)
        return g

    # @staticmethod
    # def GRAPH2():
    #     g = graph.WuGraph(9)
    #     a = g.set_edge
    #     a(0, 1, 3)
    #     a(0, 2, 7)
    #     a(0, 3, 4)
    #     a(1, 3, 9)
    #     a(2, 3, 6)
    #     a(2, 4, 2)
    #     a(3, 4, 5)
    #     a(5, 6, 4)
    #     a(5, 8, 9)
    #     a(5, 7, 3)
    #     a(6, 8, 7)
    #     a(7, 8, 12)
    #     return g
    #
    # @staticmethod
    # def GRAPH2_MST():
    #     g = graph.WuGraph(9)
    #     a = g.set_edge
    #     a(2, 4, 2)
    #     a(0, 1, 3)
    #     a(0, 3, 4)
    #     a(3, 4, 5)
    #     a(5, 7, 3)
    #     a(5, 6, 4)
    #     a(6, 8, 7)
    #     return g

    @staticmethod
    def GRAPH3():
        g = graph.WuGraph(1)
        g.set_edge(0, 0, 10)
        return g

    @staticmethod
    def GRAPH3_MST():
        g = graph.WuGraph(1)
        return g

    def test_graphs(self):
        self.assertTrue(graph._same_graph(graph._kruskal(self.GRAPH0()), self.GRAPH0_MST()))
        self.assertTrue(graph._same_graph(graph._kruskal(self.GRAPH1()), self.GRAPH1_MST()))
        # print(graph._print_graph(self.GRAPH2()))
        # print()
        # print(graph._print_graph(self.GRAPH2_MST()))
        # print()
        # print(graph._print_graph(graph._kruskal(self.GRAPH2())))
        # print()
        # self.assertTrue(graph._same_graph(graph._kruskal(self.GRAPH2()), self.GRAPH2_MST()))
        self.assertTrue(graph._same_graph(graph._kruskal(self.GRAPH3()), self.GRAPH3_MST()))


if __name__ == '__main__':
    unittest.main()
