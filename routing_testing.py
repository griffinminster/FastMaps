import routing as route
import unittest


class TestStringMethods(unittest.TestCase):
    @staticmethod
    def GRAPH0():
        g = route.graph.WuGraph(4)
        a = g.set_edge
        a(0, 1, 5)
        a(0, 2, 4)
        a(0, 3, 6)
        a(1, 2, 7)
        a()
        return g


if __name__ == '__main__':
    unittest.main()
