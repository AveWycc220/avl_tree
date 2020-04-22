""" Module for test class - AVLTree """
import sys
import unittest
sys.path.append('../')
from modules.avl_tree import AVLTree
#TODO _insert_node, _recompute_heights, _rebalance, _rrc, _rlc, _llc, _lrc, _search_for_delete,\
#TODO _search_node, delete(, _remove_leaf, _swap_and_remove, _find_smallest, _swap_nodes, _remove_branch

class TestAVLTreeMethods(unittest.TestCase):
    """ Class for test methods of tree """
    # pylint: disable=W0212
    # W0212 - Access to a protected member

    def setUP(self):
        """ Start """

    def test_init(self):
        """ Test __init__ """
        tree = AVLTree()
        self.assertEqual(tree._AVLTree__node_count, 0)
        self.assertEqual(tree._AVLTree__root, None)

    def test_node_count(self):
        """ Test getter for __node_count """
        tree_first = AVLTree()
        tree_first.insert(14)
        tree_first.insert(16)
        self.assertEqual(tree_first.node_count, 2)
        tree_empty = AVLTree()
        self.assertEqual(tree_empty.node_count, 0)

    def test_set_root(self):
        """ Test for _set_root """
        tree_root_empty = AVLTree()
        tree_root_empty._set_root(None) 
        self.assertEqual(tree_root_empty._AVLTree__root.value, None)
        tree_root_val = AVLTree()
        tree_root_val._set_root(15)
        self.assertEqual(tree_root_val._AVLTree__root.value, 15)

    def test_insert(self):
        """ Test for insert() """
        # First situation. Only one element.
        tree_first = AVLTree()
        tree_first.insert(5)
        self.assertEqual(tree_first._AVLTree__root.value, 5)
        self.assertEqual(tree_first.search(5), True)
        # Second situation. Two element.
        tree_second = AVLTree()
        tree_second.insert(5)
        tree_second.insert(10)
        self.assertEqual(tree_second._AVLTree__root.value, 5)
        self.assertEqual(tree_second.search(5), True)
        self.assertEqual(tree_second.search(10), True)
        self.assertEqual(tree_second.search(8), False)
        self.assertEqual(tree_second._AVLTree__root.value, 5)
        # Third situation. Elements : str
        tree_third = AVLTree()
        tree_third.insert("two")
        tree_third.insert("three")
        self.assertEqual(tree_third.search("two"), True)
        self.assertEqual(tree_third.search("three"), True)
        self.assertEqual(tree_third._AVLTree__root.value, "two")
    def test_search(self): 
        """ Test for search() """
        # First situation.
        tree = AVLTree()
        self.assertEqual(tree.search(5), False)
        self.assertEqual(tree.search("None"), False)
        for i in range(0, 20):
            tree.insert(i)
        self.assertEqual(tree.search(18), True)
        # Second situation. Elements : str
        tree_string = AVLTree()
        for j in range(0, 20):
            tree_string.insert(F'{j}')
        self.assertEqual(tree_string.search('12'), True)
        tree_list = AVLTree()
        tree_list.insert([5, 4, 5])
        self.assertEqual(tree_list.search([5, 4, 5]), True)
