""" Module for elements in tree """
from node import Node

class AVLTree():
    """ Class of avl_tree. """
    def __init__(self):
        """ Initialization """
        self.root = None
        self.node_count = 0
    def set_root(self, val):
        """ Set the root value """
        self.root = Node(val)
    def insert(self, val):
        """ Insert a val into AVLTree """
        if self.root is None:
            self.set_root(val)
        else:
            self._insert_node(self.root, val)
        self.node_count += 1
    def _insert_node(self, current_node, val):
        """ Help 'def insert()' to insert a value into tree. """
        node_to_rebalance = None
        if current_node.val > val:
            if current_node.left:
                self._insert_node(current_node.left, val)
            else:
                new_node = Node(val)
                current_node.left = new_node
                new_node.parent = current_node
                if current_node.height == 0:
                    self._recompute_heights(current_node)
                    node = current_node
                    while node:
                        if node.balance_factor() in [-2 , 2]:
                            node_to_rebalance = node
                            break
                        node = node.parent
        else:
            if current_node.right:
                self._insert_node(current_node.right, val)
            else:
                new_node = Node(val)
                current_node.right = new_node
                new_node.parent = current_node
                if current_node.height == 0:
                    self._recompute_heights(current_node)
                    node = current_node
                    while node:
                        if node.balance_factor() in [-2 , 2]:
                            node_to_rebalance = node
                            break
                        node = node.parent
    @classmethod
    def _recompute_heights(cls, start_node):
        """ Change height of elements after operation """
        changed = True
        node = start_node
        while node and changed:
            old_height = node.height
            node.height = (node.max_children_height() + 1 if (node.right or node.left) else 0)
            changed = node.height != old_height
            node = node.parent
