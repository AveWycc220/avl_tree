""" Module for API methods of class - AVLTree """
import sys
import unittest
sys.path.append('../')
from modules.avl_tree import AVLTree


class TestAVLTreeAPI(unittest.TestCase):
    """ Class for test API methods of tree """

    def setUp(self):
        """ Start """

    def test_max(self):
        """ Test max() for users """
        tree = AVLTree()
        self.assertEqual(tree.max(True), None)
        self.assertEqual(tree.max(), 'Tree is empty')
        tree.insert(6)
        tree.insert(2)
        tree.insert(1616)
        self.assertEqual(tree.max(True), 1616)
        self.assertEqual(tree.max(), '1616')
        tree.delete(1616)
        self.assertEqual(tree.max(True), 6)

    def test_min(self):
        """ Test for min() for users """
        tree = AVLTree()
        self.assertEqual(tree.min(True), None)
        self.assertEqual(tree.min(), 'Tree is empty')
        tree.insert(6)
        tree.insert(2)
        tree.insert(1616)
        self.assertEqual(tree.min(True), 2)
        self.assertEqual(tree.min(), '2')
        tree.delete(2)
        self.assertEqual(tree.min(True), 6)

    def test_insert(self):
        """ Test for insert() for users """
        # type(node1) != type(node2)
        tree_first = AVLTree()
        tree_first.insert(15)
        tree_first.insert("20")
        self.assertEqual(tree_first.search("20"), False)
        # Insert : int -> Delete -> Insert : str
        tree_second = AVLTree()
        tree_second.insert(15)
        tree_second.delete(15)
        tree_second.insert("15")
        self.assertEqual(tree_second.search("15"), True)

    def test_search(self):
        """ Test for search() for users """
        # type(node1) != type(node2)
        tree_first = AVLTree()
        tree_first.insert(15)
        self.assertEqual(tree_first.search("15"), False)
        # Insert : int -> Delete -> Insert : str
        tree_second = AVLTree()
        tree_second.insert(15)
        tree_second.delete(15)
        tree_second.insert("15")
        self.assertEqual(tree_second.search("15"), True)
        # Empty
        tree_third = AVLTree()
        self.assertEqual(tree_third.search(20), False)
        self.assertEqual(tree_third.search(20, True), 'None')

    def test_delete(self):
        """ Test for delete() for users """
        # Empty
        tree_first = AVLTree()
        self.assertEqual(tree_first.delete(8), False)
        # type(node1) != type(node2)
        tree_second = AVLTree()
        tree_second.insert(15)
        self.assertEqual(tree_second.delete('15'), False)


    def tearDown(self):
        """ End """