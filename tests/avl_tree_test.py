""" Module for test class - AVLTree """
import unittest
from modules.tree.avl_tree import AVLTree

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

    def test_insert_node(self):
        """ Test for _insert_node() """
        tree = AVLTree()
        tree.insert(5) # Set root
        tree._insert_node(tree._AVLTree__root, 15)
        self.assertEqual(tree.search(15), True)
        self.assertEqual(tree.search(15, True), 'Node(Value: 15, Height: 0, Right: None, Parent: 5, Left: None)')

    def test_recompute_heights(self):
        """ Test for recompute_heights() """
        tree = AVLTree()
        tree.insert(5)
        tree.insert(15)
        tree.insert(2)
        self.assertEqual(tree.search(15, True), 'Node(Value: 15, Height: 0, Right: None, Parent: 5, Left: None)')
        self.assertEqual(tree.search(5, True), 'Node(Value: 5, Height: 1, Right: 15, Parent: None, Left: 2)')
        self.assertEqual(tree.search(2, True), 'Node(Value: 2, Height: 0, Right: None, Parent: 5, Left: None)')
    
    def test_rebalance_rrc(self):
        """ Test for rebalance and rotations. RRC """
        tree_rrc = AVLTree()
        tree_rrc.insert(5)
        tree_rrc.insert(10)
        tree_rrc.insert(15)
        self.assertEqual(tree_rrc.search(5, True), 'Node(Value: 5, Height: 0, Right: None, Parent: 10, Left: None)')
        self.assertEqual(tree_rrc.search(10, True), 'Node(Value: 10, Height: 1, Right: 15, Parent: None, Left: 5)')
        self.assertEqual(tree_rrc.search(15, True), 'Node(Value: 15, Height: 0, Right: None, Parent: 10, Left: None)')

    def test_rebalance_rlc(self):
        """ Test for rebalance and rotations. RLC """
        tree_rlc = AVLTree()
        tree_rlc.insert(5)
        tree_rlc.insert(10)
        tree_rlc.insert(8)
        self.assertEqual(tree_rlc.search(5, True), 'Node(Value: 5, Height: 0, Right: None, Parent: 8, Left: None)')
        self.assertEqual(tree_rlc.search(10, True), 'Node(Value: 10, Height: 0, Right: None, Parent: 8, Left: None)')
        self.assertEqual(tree_rlc.search(8, True), 'Node(Value: 8, Height: 1, Right: 10, Parent: None, Left: 5)')

    def test_rebalance_llc(self):
        """ Test for rebalance and rotations. LLC """
        tree_llc = AVLTree()
        tree_llc.insert(5)
        tree_llc.insert(4)
        tree_llc.insert(3)
        self.assertEqual(tree_llc.search(5, True), 'Node(Value: 5, Height: 0, Right: None, Parent: 4, Left: None)')
        self.assertEqual(tree_llc.search(4, True), 'Node(Value: 4, Height: 1, Right: 5, Parent: None, Left: 3)')
        self.assertEqual(tree_llc.search(3, True), 'Node(Value: 3, Height: 0, Right: None, Parent: 4, Left: None)')

    def test_rebalance_lrc(self): 
        """ Test for rebalance and rotations. LRC """
        tree_lrc = AVLTree()
        tree_lrc.insert(10)
        tree_lrc.insert(6)
        tree_lrc.insert(8)
        self.assertEqual(tree_lrc.search(10, True), 'Node(Value: 10, Height: 0, Right: None, Parent: 8, Left: None)')
        self.assertEqual(tree_lrc.search(6, True), 'Node(Value: 6, Height: 0, Right: None, Parent: 8, Left: None)')
        self.assertEqual(tree_lrc.search(8, True), 'Node(Value: 8, Height: 1, Right: 10, Parent: None, Left: 6)')

    def test_search_for_delete(self):
        """ Test for _search_for_delete(), that return node, unlike search() """
        tree = AVLTree()
        tree.insert(10)
        tree.insert(7)
        self.assertEqual(str(type(tree._search_for_delete(10))), "<class 'modules.tree.node.Node'>")
        self.assertEqual(str(type(tree._search_for_delete(6))), "<class 'NoneType'>")
        tree_empty = AVLTree()
        self.assertEqual(str(type(tree_empty._search_for_delete(6))), "<class 'NoneType'>")

    def test_search_node(self):
        """ Test for _search_node(), that search node by recursion in search() and _search_for_delete() """
        tree = AVLTree()
        tree.insert(5)
        tree.insert(10)
        self.assertEqual(tree._search_node(tree._AVLTree__root, 5), True)
        self.assertEqual(str(tree._search_node(tree._AVLTree__root, 10, True)), 'Node(Value: 10, Height: 0, Right: None, Parent: 5, Left: None)')
        self.assertEqual(tree._search_node(tree._AVLTree__root, 15), False)
        self.assertEqual(tree._search_node(tree._AVLTree__root, 18, True), None)

    def test_delete_leaf(self):
        """ Test for delete(). First situation. _remove_leaf() """
        tree_first = AVLTree()
        tree_first.insert(5)
        tree_first.insert(10)
        tree_first.delete(10)
        self.assertEqual(tree_first.search(10), False)
        self.assertEqual(tree_first.search(5, True), 'Node(Value: 5, Height: 0, Right: None, Parent: None, Left: None)')

    def test_delete_branch(self):
        """ Test for delete(). Second situation. _remove_branch() """
        tree_second = AVLTree()
        tree_second.insert(5)
        tree_second.insert(10)
        tree_second.delete(5)
        self.assertEqual(tree_second.search(5), False)
        self.assertEqual(tree_second.search(10, True), 'Node(Value: 10, Height: 0, Right: None, Parent: None, Left: None)')

    def test_delete_swap_and_remove(self): 
        """" Test for delete(). Third situation. _swap_and_remove() """
        tree_third = AVLTree()
        tree_third.insert(5)
        tree_third.insert(10)
        tree_third.insert(2)
        tree_third.delete(5)
        self.assertEqual(tree_third.search(5), False)
        self.assertEqual(tree_third.search(10, True), 'Node(Value: 10, Height: 1, Right: None, Parent: None, Left: 2)')
        self.assertEqual(tree_third.search(2, True), 'Node(Value: 2, Height: 0, Right: None, Parent: 10, Left: None)')

    def test_find_smallest(self):
        """ Test for _find_smallest() """
        tree = AVLTree()
        tree.insert(2)
        tree.insert(3)
        tree.insert(1)
        tree.insert(0)
        self.assertEqual(str(tree._find_smallest(tree._AVLTree__root)), 'Node(Value: 0, Height: 0, Right: None, Parent: 1, Left: None)')

    def test_swap_nodes(self):
        """ Test for _swap_nodes() """
        tree = AVLTree()
        tree.insert(2)
        tree.insert(5)
        tree.insert(1)
        self.assertEqual(str(tree.search(2, True)), 'Node(Value: 2, Height: 1, Right: 5, Parent: None, Left: 1)')
        self.assertEqual(str(tree.search(5, True)), 'Node(Value: 5, Height: 0, Right: None, Parent: 2, Left: None)')
        tree._swap_nodes(tree._search_node(tree._AVLTree__root, 2, True), tree._search_node(tree._AVLTree__root, 5, True))
        self.assertEqual(str(tree.search(2, True)), 'None') # None, because 5 > 2 then search() cant fint this node
        self.assertEqual(str(tree.search(5, True)), 'Node(Value: 5, Height: 1, Right: 2, Parent: None, Left: 1)')

    def test_max(self):
        """ Test for max() """
        tree = AVLTree()
        self.assertEqual(tree.max(True), None)
        self.assertEqual(tree.max(), 'Tree is empty')
        tree.insert(6)
        tree.insert(2)
        tree.insert(1616)
        self.assertEqual(tree.max(True), 1616)
        self.assertEqual(tree.max(), '1616')

    def test_min(self):
        """ Test for min() """
        tree = AVLTree()
        self.assertEqual(tree.min(True), None)
        self.assertEqual(tree.min(), 'Tree is empty')
        tree.insert(6)
        tree.insert(2)
        tree.insert(1616)
        self.assertEqual(tree.min(True), 2)
        self.assertEqual(tree.min(), '2')
    
    def tearDown(self):
        """ End """