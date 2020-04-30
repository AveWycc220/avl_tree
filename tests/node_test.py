""" Module for test class - Node """
import unittest
from modules.tree.node import Node

class TestNode(unittest.TestCase):
    """ Class for test methods of Node """
    def setUp(self):
        """ Start """

    def test_init(self):
        """ Test __init__ """
        node_int = Node(6)
        self.assertEqual(node_int.value, 6)
        node_none = Node()
        self.assertEqual(node_none.value, None)
        node_string = Node('Hello')
        self.assertEqual(node_string.value, 'Hello')
        node_list = [2, 4]
        self.assertEqual(node_list, [2, 4])
        node_tuple = (2, 4)
        self.assertEqual(node_tuple, (2, 4))

    def test_max_children_height(self):
        """ Test max_children_height() """
        # First situation
        node_first_root = Node()
        node_first_root.height = 4
        node_first_right = Node()
        node_first_right.height = 6
        node_first_left = Node()
        node_first_left.height = 8
        node_first_root.right = node_first_right
        node_first_root.left = node_first_left
        self.assertEqual(node_first_root.max_children_height(), 8)
        # Second situation
        node_second_root = Node()
        node_second_root.height = 4
        node_second_right = Node()
        node_second_right.height = 6
        node_second_root.right = node_first_right
        self.assertEqual(node_second_root.max_children_height(), 6)
        # Third situation
        node_third_root = Node()
        node_third_root.height = 4
        node_third_left = Node()
        node_third_left.height = 8
        node_third_root.left = node_first_left
        self.assertEqual(node_third_root.max_children_height(), 8)
        # Fourth situation
        node_fourth_root = Node()
        node_fourth_root.height = 4
        self.assertEqual(node_fourth_root.max_children_height(), -1)

    def test_str(self):
        """ Test print(node) """
        node = Node(4)
        self.assertEqual(str(node), "Node(Value: 4, Height: 0, \
Right: None, Parent: None, Left: None)")

    def test_balance_factor(self):
        # First situation
        node_first_root = Node(5)
        node_first_root.height = 60
        node_first_left = Node()
        node_first_right = Node()
        node_first_root.right = node_first_right
        node_first_root.left = node_first_left
        node_first_right.height = 6
        node_first_left.height = 10
        self.assertEqual(node_first_root.balance_factor(), 4)
        # Second situation
        node_second_root = Node(5)
        node_second_root.height = 60
        node_second_left = Node()
        node_second_root.left = node_second_left
        node_second_left.height = 10
        self.assertEqual(node_second_root.balance_factor(), 11)
        # Third situation
        node_third_root = Node(5)
        node_third_root.height = 60
        node_third_right = Node()
        node_third_root.right = node_third_right
        node_third_right.height = 10
        self.assertEqual(node_third_root.balance_factor(), -11)
        # Fourth situation
        node_fourth_root = Node(5)
        self.assertEqual(node_fourth_root.balance_factor(), 0)

    def tearDown(self):
        """ End """
