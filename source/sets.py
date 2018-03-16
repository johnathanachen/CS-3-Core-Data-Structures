#!python

from hashtable import HashTable
from linkedlist import LinkedList

# Hashtables are the most common implementation of sets
class Set(object):

    def __init__(self, elements=None):
        self.data = HashTable(5)
        if elements == None:
            self.size = 0
        else:
            self.size = len(elements)

    def __repr__(self):
        return 'HashTable({!r})'.format(self.data.items())

    def contains(self, element):
        return self.data.contains(element)

    def add(self, element):
        # check to see if there is duplicates
        if element not in self.data.keys():
            self.data.set(element, None)
            self.size += 1

    def remove(self, element):
        # TODO: need to check if element doesnt exist 
        return self.data.delete(element)

    def union(self, other_set):

        # Method 1
        # new_set = Set(self.data.keys())
        #
        # for element in other_set.data.keys():
        #     if self.data.contains(element) == False:
        #         new_set.add(element)

        # Method 2
        other_set_keys = other_set.data.keys()
        current_set_keys = self.data.keys()
        combine = other_set_keys + current_set_keys
        new_set = Set(combine)

        return new_set

    def intersection(self, other_set):
        new_set = Set(self.data.keys())

        for element in other_set.data.keys():
            if self.data.contains(element):
                new_set.add(element)

        return new_set

    def difference(self, other_set):
        new_set = Set(self.data.keys())

        for element in self.data.keys():
            if other_set.data.contains(element) == False:
                new_set.add(element)

        return new_set

    def is_subset(self, other_set):
        new_set = Set(self.data.keys())

        for element in other_set.data.keys():
            if self.data.contains(element) == False:
                new_set.add(element)

        for element in self.data.keys():
            if other_set.data.contains(element) == False:
                new_set.add(element)

        return new_set


def test_set():
    my_set = Set()
    my_set.add("1")
    my_set.add("2")
    my_set.add("3")
    my_set.add("4")
    other_set = Set()
    other_set.add("3")
    other_set.add("4")
    other_set.add("5")
    other_set.add("6")

    print(my_set.intersection(other_set))


if __name__ == '__main__':
    test_set()
