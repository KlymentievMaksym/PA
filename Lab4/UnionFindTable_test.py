import unittest
from UnionFindTable import UnionFindTable


class UnionFindTableTest(unittest.TestCase):
    def test_make_sets(self):
        uf = UnionFindTable([[1, 3, 5, 7], [2, 4, 8], [6]])
        self.assertEqual(uf.make_sets(), [[1, 3, 5, 7], [2, 4, 8], [6]])

    def test_make_sets_with_empty(self):
        uf = UnionFindTable([[1], []])
        self.assertEqual(uf.make_sets(), [[1]])

    def test_find(self):
        uf = UnionFindTable([[1, 3, 5, 7], [2, 4, 8], [6]])
        self.assertEqual(uf.find(4), 2)

    def test_union(self):
        uf = UnionFindTable([[1, 3, 5, 7], [2, 4, 8], [6]])
        exceptcation = uf.make_sets()
        exceptcation[0] = exceptcation[1] + exceptcation[0]
        exceptcation[1] = []
        self.assertEqual(uf.union(1, 2).make_sets(), exceptcation)

    def test_union_with_same(self):
        uf = UnionFindTable([[1, 3, 5, 7], [2, 4, 8], [6]])
        self.assertEqual(uf.union(1, 1).make_sets(), uf.make_sets())

    def test_union_when_not_needed(self):
        uf = UnionFindTable([[1, 3, 5, 7], [2, 4, 8], [6]])
        uf.union(1, 2)
        exceptcation = uf.make_sets()
        self.assertEqual(uf.union(1, 2).make_sets(), exceptcation)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
