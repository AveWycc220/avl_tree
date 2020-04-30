""" Module of set """
from accessify import implements
from modules.set.interface_set import ISet
from modules.tree.avl_tree import AVLTree

@implements(ISet)
class Set():
    """ Class of set on avl tree """
    # pylint: disable=W0123
    # W0123 - Use of eval
    __tree = None
    __set_type = None

    def __init__(self, tree_type):
        """ Initialization """
        self.__tree = AVLTree()
        self.__set_type = tree_type

    def add(self, val):
        """ Add value in set """
        if self._conversion(val):
            self.__tree.insert(val)

    def clear(self):
        """ Delete all elements in set """
        del self.__tree
        self.__tree = AVLTree()
        print("Set is empty now")

    def remove(self, val):
        """ Remove element from set """
        if self._conversion(val):
            self.__tree.delete(val)

    def contains(self, val):
        """ Return true or node if contains, else False or None """
        if self._conversion(val):
            return self.__tree.search(val)

    def count(self):
        """ Get count of elements in set """
        return self.__tree.node_count

    def is_empty(self):
        """ Return true is not empty, else False """
        return True if self.__tree.node_count == 0 else False

    def _conversion(self, val):
        """ Convert value in needed type """
        try:
            return eval(self.__set_type)(val)
        except ValueError:
            print("ValueError: Wrong input")
            return None