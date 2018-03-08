#!python

from sets import Set
import unittest


class SetTest(unittest.TestCase):

    def test_init(self):
        test_set = Set([1, 2, 3, 4])
        assert test_set.size == 4
        test_set = Set([1, 2, 3, 4, 5, 6])
        assert test_set.size == 6

    def test_add(self):
        s = Set()
        assert s.size == 0
        s.add(1)
        assert s.size == 1
        s.add(2)
        assert s.size == 2

    def test_contains(self):
        s = Set()
        s.add(1)
        s.add(2)
        assert s.contains(1) == True
        assert s.contains(2) == True
        assert s.contains(3) == False

    def test_remove(self):
        s = Set()
        s.add(1)
        s.add(2)
        s.add(3)
        s.remove(3)
        assert s.contains(3) == False
        assert s.contains(1) == True
        assert s.contains(2) == True

    def test_union(self):
        first_set = Set([3, 4, 1, 2])
        second_set = Set([3, 4, 5, 6])
        first_set.union(second_set).size == 6


    # def test_intersection(self):
    #     first_set = Set([3, 4, 1, 2])
    #     second_set = Set([3, 4, 5, 6])
    #     assert first_set.intersection(second_set).size == 2


    def test_difference(self):
        first_set = Set([3, 4, 1, 2])
        second_set = Set([3, 4, 5, 6])
        first_set.difference(second_set).size == 2

    def test_subset(self):
        first_set = Set([3, 4, 1, 2])
        second_set = Set([3, 4, 5, 6])
        first_set.difference(second_set).size == 4
